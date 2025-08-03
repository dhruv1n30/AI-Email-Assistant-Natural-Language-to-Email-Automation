# FastAPI application entry point
from fastapi import FastAPI

from app.api.v1.endpoints import email

app = FastAPI(title="AI Email Assistant",
            description="An AI-powered email assistant that automates email generation from natural language input.",)


#Allow all origin for CORS
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(email.router, prefix="/api/v1/genai", tags=["Generative AI"])
