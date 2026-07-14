"""
Pydantic schemas for Healthcare Professionals (HCP).

These schemas define the structure of data
received from and sent to the client.
"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict


class HCPBase(BaseModel):
    doctor_name: str
    hospital: str
    specialization: str


class HCPCreate(HCPBase):
    """Schema used when creating a doctor."""
    pass


class HCPUpdate(HCPBase):
    """Schema used when updating a doctor."""
    pass


class HCPResponse(HCPBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)