from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"


    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    jobs = relationship("Job", back_populates="owner")
    profile = relationship("Profile", back_populates="user", uselist=False)