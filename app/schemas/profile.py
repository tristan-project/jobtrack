from pydantic import BaseModel
from typing import List, Optional


class ProfileBase(BaseModel):
    username: str = None
    name: str = None
    preferred_functions: Optional[List[str]] = None
    employment_type: Optional[str] = None
    about: Optional[str] = None
    experience: Optional[str] = None
    phone_number: Optional[str] = None
    languages: Optional[List[str]] = None
    profile_picture: Optional[str] = None
    skills: Optional[List[str]] = None
    hobbies: Optional[List[str]] = None
    sports: Optional[List[str]] = None
    personal_skills: Optional[List[str]] = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True