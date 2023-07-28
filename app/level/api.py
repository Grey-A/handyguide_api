from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.config import database
from app.dependencies import get_db
from app.level import schemas, services

database.DBBase.metadata.create_all(bind=database.engine)
router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Level)
def create_level(level: schemas.LevelCreate, db: Session = Depends(get_db)):
    return services.create_level(level=level, db=db)
