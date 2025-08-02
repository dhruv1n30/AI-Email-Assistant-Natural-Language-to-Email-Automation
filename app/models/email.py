# Database models related to GenAI (if applicable)
from pydantic import BaseModel

class EmailResponse(BaseModel):
    receiver_email: str
    subject: str
    body: str