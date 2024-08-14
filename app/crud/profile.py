from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.schemas.profile import ProfileCreate, ProfileUpdate


def create_profile(db: Session, user_id: int, username: str, name: str):
    db_profile = Profile(user_id=user_id, username=username, name=name)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_profile(db: Session, user_id: int):
    return db.query(Profile).filter(Profile.user_id == user_id).first()

def update_profile(db: Session, user_id: int, profile_update: ProfileUpdate):
    db_profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    if db_profile:
        for var, value in vars(profile_update).items():
            setattr(db_profile, var, value) if value else None
        db.commit()
        db.refresh(db_profile)
    return db_profile


def update_profile_item_function(db: Session, user_id: int, profile_update: ProfileUpdate):
    db_profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    if db_profile:
        for key, value in profile_update.dict(exclude_unset=True).items():
            setattr(db_profile, key, value)
        db.commit()
        db.refresh(db_profile)
    return db_profile