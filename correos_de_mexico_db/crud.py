from sqlalchemy import String
from sqlalchemy.orm import Session
from . import models

def find_cp(db: Session):
    return db.query(models.CodigoPostal.dCodigo).all()

def find_neighborhood_by_cp(cp: int, db: Session):
    return db.query(models.CodigoPostal.dAsenta).filter(models.CodigoPostal.dCodigo == cp).all()

def find_neighborhood_by_municipality(muni: str, db: Session):
    return db.query(models.CodigoPostal.dAsenta).filter(models.CodigoPostal.dMnpio == muni).all()

def find_by_cp(cp: int, db: Session):
    return db.query(models.CodigoPostal).filter(models.CodigoPostal.dCodigo == cp).all()

def find_cp_by_dMnpio(muni: str, db: Session):
    return db.query(models.CodigoPostal.dCodigo).filter(models.CodigoPostal.dMnpio == muni).all()

def find_dEstado(db: Session):
    return db.query(models.CodigoPostal.dEstado).all()

def find_municipality_by_state(state: str, db: Session):
    return db.query(models.CodigoPostal.dMnpio).filter(models.CodigoPostal.dEstado == state).all()

def find_cp_by_state(state: str, db: Session):
    return db.query(models.CodigoPostal.dCodigo).filter(models.CodigoPostal.dEstado == state).all()

def find_cp_by_coincidence(cp: str, db: Session):
    return db.query(models.CodigoPostal.dCodigo).filter(models.CodigoPostal.dCodigo.cast(String).like(cp + '%')).all()
