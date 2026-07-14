"""
Interaction Service

Contains business logic related to HCP interactions.
"""

from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.interaction import Interaction
from app.models.hcp import HCP

from app.schemas.interaction import (
    InteractionCreate,
    InteractionUpdate,
)


def get_all_interactions(db: Session):
    """
    Get all interactions.
    """
    return db.query(Interaction).all()


def get_interaction_by_id(db: Session, interaction_id: int):
    """
    Get a single interaction by ID.
    """
    return (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )


def create_interaction(db: Session, interaction: InteractionCreate):
    """
    Create a new interaction.
    """
    new_interaction = Interaction(**interaction.model_dump())

    db.add(new_interaction)
    db.commit()
    db.refresh(new_interaction)

    return new_interaction


def update_interaction(
    db: Session,
    interaction_id: int,
    updated_data: InteractionUpdate,
):
    """
    Update an existing interaction.
    """

    interaction = get_interaction_by_id(db, interaction_id)

    if interaction is None:
        return None

    for key, value in updated_data.model_dump().items():
        setattr(interaction, key, value)

    db.commit()
    db.refresh(interaction)

    return interaction


def delete_interaction(db: Session, interaction_id: int):
    """
    Delete an interaction.
    """

    interaction = get_interaction_by_id(db, interaction_id)

    if interaction is None:
        return None

    db.delete(interaction)
    db.commit()

    return interaction


def search_by_doctor(db: Session, doctor_name: str):
    """
    Search interactions by doctor's name.
    """

    return (
        db.query(Interaction)
        .join(HCP, Interaction.hcp_id == HCP.id)
        .filter(HCP.doctor_name.ilike(f"%{doctor_name}%"))
        .all()
    )


def search_by_hospital(db: Session, hospital: str):
    """
    Search interactions by hospital.
    """

    return (
        db.query(Interaction)
        .join(HCP, Interaction.hcp_id == HCP.id)
        .filter(HCP.hospital.ilike(f"%{hospital}%"))
        .all()
    )


def search_by_keyword(db: Session, keyword: str):
    """
    Search interactions by products discussed,
    discussion summary or remarks.
    """

    return (
        db.query(Interaction)
        .filter(
            or_(
                Interaction.products_discussed.ilike(f"%{keyword}%"),
                Interaction.discussion_summary.ilike(f"%{keyword}%"),
                Interaction.remarks.ilike(f"%{keyword}%"),
            )
        )
        .all()
    )
def search_by_date(db: Session, visit_date):
    """
    Search interactions by visit date.
    """

    return (
        db.query(Interaction)
        .filter(Interaction.visit_date == visit_date)
        .all()
    )

def get_interactions_by_doctor_name(
    db: Session,
    doctor_name: str,
):
    """
    Return every interaction of a doctor.
    """

    return (
        db.query(Interaction)
        .join(HCP, Interaction.hcp_id==HCP.id)
        .filter(
            HCP.doctor_name.ilike(f"%{doctor_name}%")
        )
        .order_by(Interaction.visit_date.asc())
        .all()
    )