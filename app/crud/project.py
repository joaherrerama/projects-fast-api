from sqlalchemy.orm import Session
from geoalchemy2.shape import from_shape
from app.models.project import Project
from app.schemas.project import ProjectCreate

def create_project(db: Session, project: ProjectCreate) -> Project:
    geom = from_shape(project.area_of_interest.to_shape())
    db_project = Project(
        name=project.name,
        description=project.description,
        start_date=project.start_date,
        end_date=project.end_date,
        area_of_interest=geom
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_project(db: Session, project_id: int) -> Project | None:
    return db.query(Project).filter(Project.id == project_id).first()

def get_projects(db: Session, skip: int = 0, limit: int = 100) -> list[Project]:
    return db.query(Project).offset(skip).limit(limit).all()

def delete_project(db: Session, project_id: int) -> bool:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        db.delete(project)
        db.commit()
        return True
    return False

def update_project(db: Session, project_id: int, project_data: ProjectCreate) -> Project | None:
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if db_project:
        geom = from_shape(project_data.area_of_interest.to_shape())
        update_data = project_data.dict(exclude_unset=True)
        update_data['area_of_interest'] = geom
        
        for key, value in update_data.items():
            setattr(db_project, key, value)
            
        db.commit()
        db.refresh(db_project)
        return db_project
    return None