from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey, Float, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
from uuid import uuid4
from app.database import db
import enum

class UserCategoryEnum(enum.Enum):
    Student="Student"
    Volunteer="Volunteer"

class User(db.Model):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(128), unique = True, nullable=False)
    role = Column(Enum(UserCategoryEnum, create_constraint=True, name="user_category_enum"), nullable=False)
    math = Column(Float, nullable=False)
    physics = Column(Float, nullable=False)
    chemistry = Column(Float, nullable=False)
    biology = Column(Float, nullable=False)
    literature = Column(Float, nullable=False)
    history = Column(Float, nullable=False)
    geography = Column(Float, nullable=False)
    phylosophy = Column(Float, nullable=False)
    art = Column(Float, nullable=False)
    foreign_language = Column(Float, nullable=False)
    jobs = relationship("Job", secondary="user_job")

class Job(db.Model):
    __tablename__ = "job"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(128), unique=True, nullable=False)
    average_earning = Column(Integer, nullable=False)
    users = relationship("User", secondary="user_job")

    def __init__(self, name, average_earning):
        self.name = name
        self.average_earning = average_earning
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class UserJob(db.Model):
    __tablename__ = "user_job"
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), primary_key=True)
    job_id = Column(UUID(as_uuid=True), ForeignKey("job.id"), primary_key=True)

