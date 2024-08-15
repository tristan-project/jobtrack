from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreate
from app.crud.user import get_user_by_email, create_user, get_current_user
from app.db.session import get_db


router = APIRouter()

@router.get("/me", response_model=User)
def read_users_me(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/user-data", response_model=User)
async def user_data(current_user: User = Depends(get_current_user)):
    return current_user

