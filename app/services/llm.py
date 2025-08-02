# Business logic for GenAI interactions (e.g., calling LLMs)
from models.email import EmailResponse
from openai import OpenAI
from core.config import Config


llm_key = Config.OPENAI_API_KEY
if not llm_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")


client = OpenAI(api_key=llm_key)

response = client.responses.parse(
    model="gpt-4.1-nano",
    input=[
        {"role": "system", "content": "Extract the Email information."},
        {
            "role": "user",
            "content": "Generate an email response to the based on the user natural language input",
        },
    ],

    text_format = EmailResponse
)

print(response.output_text)