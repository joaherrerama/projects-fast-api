from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator
from app.schemas.geometry import GeoJSON

class ProjectBase(BaseModel):
    name: str = Field(..., max_length=32)
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    area_of_interest: GeoJSON

    @validator('end_date')
    def validate_dates(cls, v, values):
        if 'start_date' in values and v < values['start_date']:
            raise ValueError('end_date must be after start_date')
        return v

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        from_attributes = True