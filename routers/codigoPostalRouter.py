from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from correos_de_mexico_db import crud, models
from correos_de_mexico_db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix= "/codigos-postales/v1",
    tags=["CodigosPostales"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all")
def read_codigos_postales(db: Session = Depends(get_db)):
    myset = set(crud.find_cp(db))
    mylist = list(myset)
    mylist.sort()

    return mylist

@router.get("/nbhd-by-cp/{cp}")
def read_neighborhood_by_cp(cp: int, db: Session = Depends(get_db)):
    myset = set(crud.find_neighborhood_by_cp(cp, db))
    mylist = list(myset)
    mylist.sort()

    return mylist

@router.get("/nbhd-by-muni/{muni}")
def read_neighborhood_by_municipality(muni: str, db: Session = Depends(get_db)):
    myset = set(crud.find_neighborhood_by_municipality(muni, db))
    mylist = list(myset)
    mylist.sort()

    return mylist

@router.get("/info-about-cp/{cp}")
def read_codigoPostal(cp: int, db:Session = Depends(get_db)):
    return crud.find_by_cp(cp, db)

@router.get("/cp-by-muni/{muni}")
def read_cp_by_muni(muni: str, db: Session = Depends(get_db)):
    myset = set(crud.find_cp_by_dMnpio(muni, db))
    mylist = list(myset)
    mylist.sort()

    return mylist

@router.get("/states")
def read_states(db: Session = Depends(get_db)):
    myset = set(crud.find_dEstado(db))
    mylist = list(myset)
    mylist.sort()

    return mylist

@router.get("/muni-by-state/{state}")
def read_muni_by_state(state: str, db: Session = Depends(get_db)):
    myset = set(crud.find_municipality_by_state(state, db))
    mylist = list(myset)
    mylist.sort()

    return mylist

@router.get("/cp-by-state/{state}")
def read_cp_by_state(state: str, db: Session = Depends(get_db)):
    myset = set(crud.find_cp_by_state(state, db))
    mylist = list(myset)
    mylist.sort()

    return mylist

@router.get("/search-cp/{cp}")
def read_cp_by_coincidence(cp: str, db: Session = Depends(get_db)):
    myset = set(crud.find_cp_by_coincidence(cp, db))
    mylist = list(myset)
    mylist.sort()

    return mylist