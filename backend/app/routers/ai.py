"""
AI Router

Provides AI endpoints for the React frontend.

The frontend sends natural language.

The backend returns structured JSON that
automatically fills the Log Interaction form.
"""
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_database

from app.services import hcp_service
from app.services import interaction_service

from app.schemas.hcp import HCPCreate
from app.schemas.interaction import InteractionCreate
from fastapi import APIRouter

from app.schemas.ai import ChatRequest

from app.langgraph.agent import agent

router = APIRouter(
    prefix="/ai",
    tags=["AI Assistant"]
)


@router.post("/chat")
def ai_chat(request: ChatRequest):
    """
    Route every chat request through LangGraph.
    """

    result = agent.invoke(
        {
            "message": request.message
        }
    )
    

    return {
        "tool": result["tool"],
        "data": result["result"],
    }
@router.post("/save-interaction")
def save_interaction_ai(
    payload: dict,
    db: Session = Depends(get_database),
):

    doctor_name = payload.get("doctor_name", "")

    doctor_name = (
        doctor_name
        .replace("Doctor", "")
        .replace("doctor", "")
        .replace("Dr.", "")
        .replace("Dr", "")
        .strip()
    )

    hospital = payload.get("hospital")

    doctor = hcp_service.get_hcp_by_name(
        db,
        doctor_name,
    )

    if doctor is None:

        doctor = hcp_service.create_hcp(
            db,
            HCPCreate(
                doctor_name=doctor_name,
                hospital=hospital,
                specialization="Unknown",
            ),
        )

    interaction = InteractionCreate(
        hcp_id=doctor.id,
        interaction_type=payload.get("interaction_type"),
        visit_date=payload.get("visit_date"),
        visit_time=None,
        attendees=hospital,
        topics_discussed=payload.get(
            "discussion_summary"
        ),
        products_discussed=payload.get(
            "products_discussed"
        ),
        discussion_summary=payload.get(
            "discussion_summary"
        ),
        materials_shared=payload.get(
            "products_discussed"
        ),
        samples_distributed=payload.get(
            "samples_distributed"
        ),
        sentiment=payload.get("sentiment"),
        outcomes=payload.get("outcomes"),
        follow_up_actions=None,
        follow_up_date=payload.get(
            "follow_up_date"
        ),
        remarks=payload.get("remarks"),
    )

    saved = interaction_service.create_interaction(
        db,
        interaction,
    )

    return {
        "message": "Interaction saved successfully",
        "interaction_id": saved.id,
        "doctor_id": doctor.id,
    }