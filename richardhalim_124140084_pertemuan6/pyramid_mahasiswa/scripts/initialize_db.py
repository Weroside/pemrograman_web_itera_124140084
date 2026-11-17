from sqlalchemy.dialects.postgresql import insert

from pyramid_mahasiswa.models import Mahasiswa, Matakuliah
from pyramid_mahasiswa.models.meta import buat_engine


def main():
    engine = buat_engine()
    mahasiswa = [
        dict(nim="DEMO01", nama="Nabila", jurusan="Informatika"),
        dict(nim="DEMO02", nama="Raka", jurusan="Informatika"),
    ]
    matakuliah = [
        dict(kode_mk="IF2110", nama_mk="Pemrograman Web", sks=3, semester=3),
        dict(kode_mk="IF3140", nama_mk="Basis Data", sks=4, semester=5),
        dict(kode_mk="IF2201", nama_mk="Struktur Data", sks=3, semester=4),
    ]
    with engine.begin() as conn:
        for model, data, kunci in (
            (Mahasiswa, mahasiswa, "nim"), (Matakuliah, matakuliah, "kode_mk")
        ):
            stmt = insert(model).values(data)
            conn.execute(stmt.on_conflict_do_nothing(index_elements=[kunci]))
    engine.dispose()
    print("Data awal tersedia.")


if __name__ == "__main__":
    main()
