from sqlalchemy import Column, Integer, String
from .database import Base

class CodigoPostal(Base):
    __tablename__ = "codigos_postales"

    dCodigo = Column("d_codigo", Integer)
    dAsenta = Column("d_asenta", String)
    dTipoAsenta = Column("d_tipo_asenta", String)
    dMnpio = Column("d_mnpio", String)
    dEstado = Column("d_estado", String)
    dCiudad = Column("d_ciudad", String)
    dCp = Column("d_cp", Integer)
    cEstado = Column("c_estado", Integer)
    cOficina = Column("c_oficina", Integer)
    cCp = Column("c_cp", Integer)
    cTipoAsenta = Column("c_tipo_asenta", Integer)
    cMnpio = Column("c_mnpio", Integer)
    id = idAsentaCpcons = Column("id_asenta_cpcons", Integer, primary_key = True)
    dZona = Column("d_zona", String)
    cCveCiudad = Column("c_cve_ciudad", Integer)