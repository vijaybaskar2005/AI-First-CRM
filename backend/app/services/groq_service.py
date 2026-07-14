"""
Groq Service

This file creates a reusable Groq client.

All LangGraph tools will use this service instead of
creating multiple Groq clients.
"""

from groq import Groq

from app.config.settings import settings


class GroqService:
    """
    Handles communication with Groq LLM.
    """

    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = settings.GROQ_MODEL

    def chat(self, prompt: str) -> str:
        """
        Sends a prompt to the Groq model
        and returns the generated response.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant for a Healthcare CRM. "
                        "Always return only valid JSON when asked to extract information."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content