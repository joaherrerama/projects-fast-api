from sqlalchemy import Column, Integer, String, DateTime
from geoalchemy2 import Geometry
from app.db.base import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), nullable=False, index=True)
    description = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    area_of_interest = Column(Geometry('GEOMETRY'), nullable=False)