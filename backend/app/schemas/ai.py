"""
AI Schemas

These schemas define the request and response models
used by the AI Assistant.
"""

from typing import Optional, Dict, Any

from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Request received from the frontend AI chat.
    """
    message: str


class ExtractedInteraction(BaseModel):
    """
    Structured interaction extracted by the LLM.
    """

    doctor_name: Optional[str] = None

    hospital: Optional[str] = None

    interaction_type: Optional[str] = "Meeting"

    visit_date: Optional[str] = None

    visit_time: Optional[str] = None

    products_discussed: Optional[str] = None

    discussion_summary: Optional[str] = None

    samples_distributed: Optional[str] = None

    sentiment: Optional[str] = "Neutral"

    outcomes: Optional[str] = None

    follow_up_date: Optional[str] = None

    remarks: Optional[str] = None


class AgentResponse(BaseModel):
    """
    Generic response returned by every LangGraph tool.
    """

    tool: str

    data: Dict[str, Any]


class ChatResponse(AgentResponse):
    """
    Backward compatible alias.
    """
    pass