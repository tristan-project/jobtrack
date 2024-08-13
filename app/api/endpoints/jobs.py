import logging
from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.job import JobCreate, Job, JobUpdate
from app.crud.job import create_job, get_job, get_job_by_id, get_jobs
from app.db.session import get_db
from typing import List
from app.crud.user import get_current_user
from sqlalchemy import Integer


router = APIRouter()


# @router.post("/register", response_model=User)
# def register_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return create_user(db=db, user=user)


@router.post("/createjob", response_model=Job)
def create_job_route(job: JobCreate, db: Session = Depends(get_db)):
    # Ensure `create_job` function in CRUD accepts these parameters
    try:
        new_job = create_job(db=db, title=job.title, description=job.description, owner_id=int(job.owner_id))
        return new_job
    except Exception as e:
        logging.error(f"Error creating job: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


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

@router.delete("/{job_id}", response_model=Job)
def delete_job(job_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    job = get_job_by_id(db, job_id=job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    if job.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this job")
    db.delete(job)
    db.commit()
    return job

@router.put("/{job_id}", response_model=Job)
def update_job(job_id: int, job_update: JobUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    job = get_job_by_id(db, job_id=job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    if job.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this job")
    
    job.title = job_update.title
    job.description = job_update.description
    db.commit()
    db.refresh(job)
    return job