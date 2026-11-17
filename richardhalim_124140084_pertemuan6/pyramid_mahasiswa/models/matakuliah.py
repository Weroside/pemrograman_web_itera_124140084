from sqlalchemy import Column, Integer, Text

from .meta import Base


class Matakuliah(Base):
    __tablename__ = "matakuliah"

    id = Column(Integer, primary_key=True, autoincrement=True)
    kode_mk = Column(Text, nullable=False, unique=True)
    nama_mk = Column(Text, nullable=False)
    sks = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)

    def to_dict(self):
        return {key: getattr(self, key)
                for key in ("id", 'kode_mk', 'nama_mk', 'sks', 'semester')}
