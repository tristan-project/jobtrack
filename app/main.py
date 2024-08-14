# Tristan Berkmans 
# r0784105
from fastapi import Depends, FastAPI
from app.api.endpoints import auth, jobs, users, profile
from app.core.config import settings
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.db.create_db import init_db
from app.core.security import verify_token

from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(title=settings.PROJECT_NAME)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify the frontend URL, e.g., ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

# Include routers from different endpoints
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(profile.router, prefix="/profile", tags=["profile"])

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/test")
def read_root():
    return {"message": "Welcome to the Job Finder API"}

@app.get("")
async def read_index():
    return FileResponse("static/auth/login.html")


@app.get("/users/create_users.html")
async def read_index():
    return FileResponse("static/users/create_users.html")


@app.get("/auth/login.html")
async def read_index():
    return FileResponse("static/auth/login.html")


@app.get("/auth/register.html")
async def read_index():
    return FileResponse("static/auth/register.html")



# @app.get("/auth/homepage.html")
# def homepage(token: str = Depends(verify_token)):
#     email = token.get("sub")
#     return FileResponse("/frontend/app/homepage.html")