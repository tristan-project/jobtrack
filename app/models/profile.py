from sqlalchemy import Column, Integer, String, Text, Enum, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import get_db
from app.db.base import Base



class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String)
    preferred_functions = Column(JSON)  # Example: ["horica", "computerscience"]
    employment_type = Column(Enum("admin", "employer", "company", "fulltime", "parttime", "flexi"))
    about = Column(Text)
    experience = Column(Text)
    phone_number = Column(String)
    languages = Column(JSON)  # Example: ["English", "Spanish"]
    profile_picture = Column(String, nullable=True)  # URL or file path
    skills = Column(JSON)  # Example: ["Python", "Django"]
    hobbies = Column(JSON)  # Example: ["Reading", "Traveling"]
    sports = Column(JSON)  # Example: ["Football", "Basketball"]
    personal_skills = Column(JSON)  # Example: ["Leadership", "Teamwork"]

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="profile")