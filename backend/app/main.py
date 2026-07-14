"""
main.py

Entry point of the AI-First CRM Backend.

Responsibilities:
- Create the FastAPI application
- Configure metadata
- Register routers (later)
- Health check endpoint
"""

from fastapi import FastAPI
from app.database.database import Base, engine
import app.models
from app.routers import hcp
from app.routers import interaction
from app.routers import ai
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI-First CRM API",
    description="Backend API for Healthcare Professional CRM",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(hcp.router)
app.include_router(interaction.router)
app.include_router(ai.router)
@app.get("/")
def root():
    return {
        "message": "Welcome to AI-First CRM Backend"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "AI-First CRM",
        "version": "1.0.0"
    }