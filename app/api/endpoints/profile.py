from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.profile import create_profile, get_profile, update_profile, update_profile_item_function
from app.schemas.profile import Profile, ProfileCreate, ProfileUpdate
from app.db.session import get_db
from app.crud.user import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=Profile)
def create_profile_endpoint(profile: ProfileCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_profile(db=db, profile=profile, user_id=user)

@router.get("/", response_model=Profile)
def read_profile(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    db_profile = get_profile(db=db, user_id=user.id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile

@router.put("/", response_model=Profile)
def update_profile_endpoint(profile_update: ProfileUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    db_profile = update_profile(db=db, user_id=user.id, profile_update=profile_update)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile


@router.patch("/", response_model=Profile)
async def update_profile_item(profile_data: ProfileUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    updated_profile = update_profile_item_function(db=db, user_id=user.id, profile_update=profile_data)
    if updated_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    return updated_profile