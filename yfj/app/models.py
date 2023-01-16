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
    __table_args__ = (
        CheckConstraint("math>=0 AND math<=10"),
        CheckConstraint("physics>=0 AND physics<=10"),
        CheckConstraint("chemistry>=0 AND chemistry<=10"),
        CheckConstraint("biology>=0 AND biology<=10"),
        CheckConstraint("literature>=0 AND literature<=10"),
        CheckConstraint("history>=0 AND history<=10"),
        CheckConstraint("geography>=0 AND geography<=10"),
        CheckConstraint("phylosophy>=0 AND phylosophy<=10"),
        CheckConstraint("art>=0 AND art<=10"),
        CheckConstraint("foreign_language>=0 AND foreign_language<=10"),
    )
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(128), unique = True, nullable=False)
    role = Column(Enum(UserCategoryEnum, create_constraint=True, name="user_category_enum_ct"), nullable=False)
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
    
    def __init__(self):
        self.username = ""
        self.role = "Student"
        self.math = 0
        self.physics = 0
        self.chemistry = 0
        self.biology = 0
        self.literature = 0
        self.history = 0
        self.geography = 0
        self.phylosophy = 0
        self.art = 0
        self.foreign_language = 0        
    def __init__(self, username, role, math, physics, chemistry, biology, literature, history, geography, phylosophy, art, foreign_language):
        self.username = username
        self.role = role
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology
        self.literature = literature
        self.history = history
        self.geography = geography
        self.phylosophy = phylosophy
        self.art = art
        self.foreign_language = foreign_language
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    def update(self):
        db.session.commit()
        return self
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def to_json(self):
        return {
            'id': self.id,
            'role': self.role.name,
            'math': self.math,
            'physics': self.physics,
            'chemistry': self.chemistry,
            'biology': self.biology,
            'literature': self.literature,
            'history': self.history,
            'geography': self.geography,
            'phylosophy': self.phylosophy,
            'art': self.art,
            'foreign_language': self.foreign_language
        }

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
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "average_earning": self.average_earning
        }

class UserJob(db.Model):
    __tablename__ = "user_job"
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), primary_key=True)
    job_id = Column(UUID(as_uuid=True), ForeignKey("job.id"), primary_key=True)

