from pydantic import BaseModel

class CodigoPostal(BaseModel):
    dCodigo: int
    dAsenta: str
    dTipoAsenta: str
    dMnpio: str
    dEstado: str
    dCiudad: str
    dCp: int
    cEstado: int
    cOficina: int
    cCp: int
    cTipoAsenta: int
    cMnpio: int
    idAsentaCpcons: int
    dZona: str
    cCveCiudad: int

    class Config:
        orm_mode = True