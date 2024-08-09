# Tristan Berkmans 
# r0784105
from fastapi import Depends, FastAPI
from app.api.endpoints import auth, jobs, users
from app.core.config import settings
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.db.create_db import init_db
from app.core.security import verify_token





app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
def on_startup():
    init_db()

# Include routers from different endpoints
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
app.include_router(users.router, prefix="/users", tags=["users"])

app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/test")
def read_root():
    return {"message": "Welcome to the Job Finder API"}

@app.get("/")
async def read_index():
    return FileResponse("frontend/index.html")


@app.get("/users/create_users.html")
async def read_index():
    return FileResponse("frontend/users/create_users.html")


@app.get("/auth/login.html")
async def read_index():
    return FileResponse("frontend/auth/login.html")


@app.get("/auth/register.html")
async def read_index():
    return FileResponse("frontend/auth/register.html")



@app.get("/auth/homepage.html")
def homepage(token: str = Depends(verify_token)):
    email = token.get("sub")
    return FileResponse("/frontend/app/homepage.html")