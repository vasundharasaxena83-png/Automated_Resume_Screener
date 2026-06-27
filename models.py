from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from backend.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    filename = Column(String)
    resume_text = Column(Text)
    jd_text = Column(Text)

    ats_score = Column(Float)
    ai_feedback = Column(Text)