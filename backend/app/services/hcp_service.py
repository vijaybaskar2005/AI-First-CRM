"""
HCP Service

Contains all business logic related to Healthcare Professionals.
Routers should call these functions instead of directly writing SQL queries.
"""

from sqlalchemy.orm import Session

from app.models.hcp import HCP
from app.schemas.hcp import HCPCreate, HCPUpdate


def get_all_hcps(db: Session):
    return db.query(HCP).all()


def get_hcp_by_id(db: Session, hcp_id: int):
    return db.query(HCP).filter(HCP.id == hcp_id).first()


def create_hcp(db: Session, hcp: HCPCreate):

    new_hcp = HCP(
        doctor_name=hcp.doctor_name,
        hospital=hcp.hospital,
        specialization=hcp.specialization or "Unknown"
    )

    db.add(new_hcp)
    db.commit()
    db.refresh(new_hcp)

    return new_hcp


def update_hcp(db: Session, hcp_id: int, updated_data: HCPUpdate):

    doctor = get_hcp_by_id(db, hcp_id)

    if doctor is None:
        return None

    doctor.doctor_name = updated_data.doctor_name
    doctor.hospital = updated_data.hospital
    doctor.specialization = updated_data.specialization

    db.commit()
    db.refresh(doctor)

    return doctor


def delete_hcp(db: Session, hcp_id: int):

    doctor = get_hcp_by_id(db, hcp_id)

    if doctor is None:
        return None

    db.delete(doctor)
    db.commit()

    return doctor
def get_hcp_by_name(db: Session, doctor_name: str):
    return (
        db.query(HCP)
        .filter(HCP.doctor_name == doctor_name)
        .first()
    )