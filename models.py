from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Subjects(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    teacher = Column(String)
    description = Column(String)
    year_long = Column(Boolean)
    credits = Column(String)
