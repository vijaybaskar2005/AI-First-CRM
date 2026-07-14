"""
Interaction model.

Stores every interaction between a Medical Representative
and a Healthcare Professional (Doctor).
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    Time,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_id = Column(Integer, ForeignKey("hcps.id"), nullable=False)

    interaction_type = Column(String(50), nullable=False)

    visit_date = Column(Date, nullable=False)

    visit_time = Column(Time)

    attendees = Column(Text)

    topics_discussed = Column(Text)

    products_discussed = Column(Text)

    discussion_summary = Column(Text)

    materials_shared = Column(Text)

    samples_distributed = Column(Text)

    sentiment = Column(String(20))

    outcomes = Column(Text)

    follow_up_actions = Column(Text)

    follow_up_date = Column(Date)

    remarks = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    doctor = relationship("HCP")