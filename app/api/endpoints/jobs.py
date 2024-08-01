from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.job import JobCreate, Job
from app.crud.job import create_job, get_job, get_jobs
from app.db.session import get_db
from typing import List
from app.api.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=Job)
def create_new_job(job: JobCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_job(db=db, job=job, user_id=current_user.id)

@router.get("/{job_id}", response_model=Job)
def read_job(job_id: int, db: Session = Depends(get_db)):
    db_job = get_job(db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

@router.get("/", response_model=List[Job])
def read_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    jobs = get_jobs(db, skip=skip, limit=limit)
    return jobs