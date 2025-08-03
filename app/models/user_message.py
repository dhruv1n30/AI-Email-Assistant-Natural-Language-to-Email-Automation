from pydantic import BaseModel


class UserMessage(BaseModel):
    to_email : str
    message: str
    sender_name : str
