"""
Pydantic schemas for Interaction.

These schemas validate incoming request data
and define response models.
"""

from datetime import date, time, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class InteractionBase(BaseModel):
    hcp_id: int

    interaction_type: str

    visit_date: date

    visit_time: Optional[time] = None

    attendees: Optional[str] = None

    topics_discussed: Optional[str] = None

    products_discussed: Optional[str] = None

    discussion_summary: Optional[str] = None

    materials_shared: Optional[str] = None

    samples_distributed: Optional[str] = None

    sentiment: Optional[str] = None

    outcomes: Optional[str] = None

    follow_up_actions: Optional[str] = None

    follow_up_date: Optional[date] = None

    remarks: Optional[str] = None


class InteractionCreate(InteractionBase):
    pass


class InteractionUpdate(InteractionBase):
    pass


class InteractionResponse(InteractionBase):
    id: int

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)