from sqlalchemy.orm import Session

from . import database_models, models


def get_graves(db: Session, grave_id: int):
    return db.query(database_models.Burial).filter(database_models.Burial.id == grave_id).first()


def get_grave_by_name(db: Session, name: str):
    tag = '%' + name + '%';
    return db.query(database_models.Burial).filter(database_models.Burial.name.like(tag)).offset(0).limit(10)


def get_graves(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database_models.Burial).offset(skip).limit(limit).all()


def create_grave(db: Session, grave: models.Grave):
    db_grave = database_models.Burial(name=grave.name
                                      , slots=grave.slots
                                      , garden=grave.garden
                                      , section=grave.section
                                      , lot=grave.lot
                                      , block=grave.block
                                      , space=grave.space)

    db.add(db_grave)
    db.commit()
    db.refresh(db_grave)
    return db_grave