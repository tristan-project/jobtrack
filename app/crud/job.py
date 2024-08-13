from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job import JobCreate

def get_job(db: Session, job_id: int):
    return db.query(Job).filter(Job.id == job_id).first()

def create_job(db: Session, title: str, description: str, owner_id: int) -> Job:
    db_job =  Job(
        title= title,
        description= description,
        owner_id= owner_id
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_jobs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Job).offset(skip).limit(limit).all()