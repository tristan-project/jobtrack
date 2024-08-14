from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.crud.profile import create_profile
from app.schemas.user import UserCreate, User  # Using your provided User schema
from app.models.user import User as UserModel
from app.crud.user import create_user, get_current_user, get_user_by_email
from app.db.session import get_db
from app.core.security import verify_password, create_access_token, oauth2_scheme, verify_token

router = APIRouter()

class LoginResponse(BaseModel):
    access_token: str
    token_type: str

# @router.post("/register", response_model=User)
# def register_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return create_user(db=db, user=user)

class RegisterRequest(BaseModel):
    email: str
    password: str
    profile: dict  # Adjust according to the profile fields

@router.post("/register")
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email= request.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # user_data = {
    #     "email": request.email,
    #     "password": request.password
    # }

    # Create User
    user = create_user(db = db, email = request.email, password = request.password)
    
    # Create Profile
    profile_data = request.profile
    profile_data['user_id'] = user.id  # Associate profile with user
    create_profile(db, **profile_data)

    return {"message": "User registered successfully!"}


@router.post("/login", response_model=LoginResponse)
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.email, "id": db_user.id})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/homepage", response_class=HTMLResponse)
async def homepage(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return FileResponse("static/app/homepage.html")

@router.get("/user-data", response_model=User)
async def user_data(current_user: User = Depends(get_current_user)):
    return current_user