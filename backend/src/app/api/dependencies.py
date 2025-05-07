from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import get_current_user, oauth2_scheme
from app.db.session import SessionLocal
from app.models.user import User
from app.schemas.token import TokenPayload

def get_db() -> Generator[Session, None, None]:
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()