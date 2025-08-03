import json

from openai import OpenAI

from app.core.config import Config
from app.models.email_response import EmailResponse


google_key = Config.GOOGLE_API_KEY

# print(google_key)

if not google_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")


client = OpenAI(api_key=google_key,
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

def call_genai_model(email_request):
    sender_name = email_request.sender_name
    completion = client.beta.chat.completions.parse(
    model="gemini-2.0-flash",
    messages=[
        {"role": "system", "content": "You are an assistant that writes professional emails"},
        {"role": "user","content": (
                    f"Generate a JSON with 'subject' and 'body' for an email based on the following message:\n"
                    f"{email_request.message}\n\n"
                    f"Make sure to sign the email with:\n\nSincerely,\n{sender_name}"
                )},
    ],
    response_format=EmailResponse,
    )

    content = completion.choices[0].message.parsed
    return json.dumps(content.model_dump(), indent = 2)

# print(completion.choices[0].message.parsed)


if __name__ == "__main__":
    email_request = "Hello, I would like to know more about your services."
    response = call_genai_model(email_request)
    print(response)

    # response = client.responses.parse(
    #     model="google/gemini-2.5-flash",
    #     input=[
    #         {"role": "system", "content": "Extract the Email information."},
    #         {
    #             "role": "user",
    #             "content": f"Generate an email response to the based on the user natural language input :{email_request}",
    #         },
    #     ],

    #     text_format = EmailResponse
    # )

    # return response.output_text
