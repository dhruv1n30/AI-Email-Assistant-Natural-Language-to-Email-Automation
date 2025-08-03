# Database models related to GenAI (if applicable)
from pydantic import BaseModel


class EmailResponse(BaseModel):
    subject: str
    body: str
