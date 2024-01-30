from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from service import models, database_models, crud
from service.database import SessionLocal

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"title": "Cemetry Service"}


# create grave
@app.post("/graves", response_model=models.Grave)
async def create_grave(grave: models.Grave, db: Session = Depends(get_db)):
    return crud.create_grave(db=db, grave=grave)


# fetch all graves
@app.get("/graves/all", response_model=list[models.Grave])
async def get_all_graves(db: Session = Depends(get_db)):
    return crud.get_graves(db=db)


# fetch grave by name
@app.get("/graves", response_model=list[models.Grave])
async def get_grave_by_name(name: str, db: Session = Depends(get_db)):
    return crud.get_grave_by_name(db=db, name=name)
