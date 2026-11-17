from sqlalchemy import Column, Integer, Text

from .meta import Base


class Mahasiswa(Base):
    __tablename__ = "mahasiswa"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nim = Column(Text, nullable=False, unique=True)
    nama = Column(Text, nullable=False)
    jurusan = Column(Text, nullable=False)

    def to_dict(self):
        return {key: getattr(self, key)
                for key in ("id", 'nim', 'nama', 'jurusan')}
