"""
Database dependency.

Provides a database session to FastAPI routes.
"""

from sqlalchemy.orm import Session

from app.database.database import get_db


def get_database() -> Session:
    yield from get_db()