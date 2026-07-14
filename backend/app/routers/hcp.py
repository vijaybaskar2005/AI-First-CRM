"""
HCP Router

Provides CRUD APIs for Healthcare Professionals.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_database
from app.schemas.hcp import (
    HCPCreate,
    HCPUpdate,
    HCPResponse
)

from app.services import hcp_service

router = APIRouter(
    prefix="/hcp",
    tags=["Healthcare Professionals"]
)


@router.get("/", response_model=list[HCPResponse])
def get_all(db: Session = Depends(get_database)):
    return hcp_service.get_all_hcps(db)

@router.get("/search", response_model=HCPResponse)
def search_hcp(
    doctor_name: str,
    db: Session = Depends(get_database)
):
    doctor = hcp_service.get_hcp_by_name(
        db,
        doctor_name
    )

    if doctor is None:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    return doctor
@router.get("/{hcp_id}", response_model=HCPResponse)
def get_one(hcp_id: int, db: Session = Depends(get_database)):

    doctor = hcp_service.get_hcp_by_id(db, hcp_id)

    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


@router.post("/", response_model=HCPResponse)
def create(
    hcp: HCPCreate,
    db: Session = Depends(get_database)
):
    return hcp_service.create_hcp(db, hcp)


@router.put("/{hcp_id}", response_model=HCPResponse)
def update(
    hcp_id: int,
    hcp: HCPUpdate,
    db: Session = Depends(get_database)
):

    doctor = hcp_service.update_hcp(db, hcp_id, hcp)

    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


@router.delete("/{hcp_id}")
def delete(
    hcp_id: int,
    db: Session = Depends(get_database)
):

    doctor = hcp_service.delete_hcp(db, hcp_id)

    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return {
        "message": "Doctor deleted successfully"
    }