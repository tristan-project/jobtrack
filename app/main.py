# Tristan Berkmans 
# r0784105
from fastapi import FastAPI
from app.api.endpoints import auth, jobs, users
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Include routers from different endpoints
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Finder API"}