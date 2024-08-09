from pydantic import BaseModel
from datetime import datetime

class JobBase(BaseModel):
    title: str
    description: str
    owner_id: int

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    date_posted: datetime
    owner_id: int

    class Config:
        orm_mode = True