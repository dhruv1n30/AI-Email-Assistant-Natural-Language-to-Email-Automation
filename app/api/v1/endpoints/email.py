
from fastapi import APIRouter, HTTPException
from loguru import logger
from pydantic import ValidationError

from app.models.email_response import EmailResponse
from app.models.user_message import UserMessage
from app.services.gmail_sender import send_email
from app.services.llm import call_genai_model
from app.utils.helper import get_credentials

router = APIRouter()


# @router.post("/generate-email")
# async def generate_email(email_request: UserMessage):
#     email_content = await call_genai_model(email_request)
#     return {"generated_email": email_content}

@router.get("/health")
def health_check():
    return "API is Healthy"


@router.post("/generate-and-send")
def generate_and_send(email_request: UserMessage):
    # Call GenAI to get structured email response
    try:
        genai_email_resp = call_genai_model(email_request)
        email_resp = EmailResponse.model_validate_json(genai_email_resp)
        logger.success(email_resp)
    except ValidationError as ve:
        raise HTTPException(status_code=400, detail=f"GenAI output validation error: {ve}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GenAI generation failed: {e}")

    # Use parsed subject and body
    subject = email_resp.subject
    body = email_resp.body

    # Send the email
    try:
        creds = get_credentials()
        send_email(subject, body, email_request.to_email, creds)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Email sending failed: {e}")

    return {"message": "Email sent successfully!", "subject": subject, "body": body}


