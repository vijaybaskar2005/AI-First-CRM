"""
Interaction Router

Provides CRUD APIs for HCP Interactions.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_database

from app.schemas.interaction import (
    InteractionCreate,
    InteractionUpdate,
    InteractionResponse,
)

from app.services import interaction_service
from app.services import hcp_service

router = APIRouter(
    prefix="/interaction",
    tags=["Interactions"],
)


@router.get("/", response_model=list[InteractionResponse])
def get_all_interactions(db: Session = Depends(get_database)):
    return interaction_service.get_all_interactions(db)


@router.get("/{interaction_id}", response_model=InteractionResponse)
def get_interaction(interaction_id: int, db: Session = Depends(get_database)):
    interaction = interaction_service.get_interaction_by_id(
        db, interaction_id
    )

    if interaction is None:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found",
        )

    return interaction


@router.post("/", response_model=InteractionResponse)
def create_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_database),
):
    doctor = hcp_service.get_hcp_by_id(db, interaction.hcp_id)

    if doctor is None:
        raise HTTPException(
            status_code=404,
            detail="Selected doctor does not exist",
        )

    return interaction_service.create_interaction(
        db,
        interaction,
    )


@router.put("/{interaction_id}", response_model=InteractionResponse)
def update_interaction(
    interaction_id: int,
    interaction: InteractionUpdate,
    db: Session = Depends(get_database),
):
    doctor = hcp_service.get_hcp_by_id(db, interaction.hcp_id)

    if doctor is None:
        raise HTTPException(
            status_code=404,
            detail="Selected doctor does not exist",
        )

    updated = interaction_service.update_interaction(
        db,
        interaction_id,
        interaction,
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found",
        )

    return updated


@router.delete("/{interaction_id}")
def delete_interaction(
    interaction_id: int,
    db: Session = Depends(get_database),
):
    deleted = interaction_service.delete_interaction(
        db,
        interaction_id,
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found",
        )

    return {
        "message": "Interaction deleted successfully"
    }