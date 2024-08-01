from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import User
from app.crud.user import get_user_by_email
from app.db.session import get_db

router = APIRouter()

@router.get("/me", response_model=User)
def read_users_me(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)): # type: ignore
    return current_user