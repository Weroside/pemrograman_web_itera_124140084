# Pertemuan 6 - API Data Akademik

**Richard Halim | NIM 124140084 | Kelas RA**

API Pyramid untuk data mahasiswa dan mata kuliah. SQLAlchemy menghubungkan
aplikasi ke PostgreSQL. Alembic membuat kedua tabel secara berurutan.

## Menjalankan

Buka folder ini di terminal. Buat database kosong bernama `paw6` di
PostgreSQL, misalnya dengan `createdb -U postgres paw6`. Lalu, di PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
$env:DATABASE_URL = 'postgresql+psycopg2://postgres:PASSWORD@127.0.0.1:5432/paw6'
alembic -c development.ini upgrade head
python -m pyramid_mahasiswa.scripts.initialize_db
pserve development.ini --reload
```

Ganti `PASSWORD`, pengguna, dan port sesuai PostgreSQL lokal. Pada
Linux/macOS gunakan `source .venv/bin/activate` dan `export DATABASE_URL=...`.
Server tersedia di `http://127.0.0.1:6543`. Untuk menjalankan tanpa reload,
gunakan `pserve production.ini`. Skrip data awal dapat dijalankan ulang
tanpa menduplikasi NIM atau kode mata kuliah.

## Struktur

- `models/`: skema dan serialisasi JSON.
- `alembic/`: migrasi tabel mahasiswa, lalu mata kuliah.
- `routes.py`: rute dengan predikat metode HTTP.
- `views/`: operasi CRUD dan validasi masukan.
- `scripts/initialize_db.py`: pengisian data awal, termasuk tiga mata kuliah.

## Endpoint

Kedua koleksi (`/api/mahasiswa` dan `/api/matakuliah`) menyediakan:

| Metode | Jalur relatif | Kegunaan |
| --- | --- | --- |
| GET | koleksi | Tampilkan daftar |
| GET | koleksi/{id} | Tampilkan satu data |
| POST | koleksi | Tambah data |
| PUT | koleksi/{id} | Ubah kolom yang dikirim |
| DELETE | koleksi/{id} | Hapus data |

POST mahasiswa memerlukan `nim`, `nama`, dan `jurusan`. POST mata kuliah
memerlukan `kode_mk`, `nama_mk`, `sks`, dan `semester`. Kode mata kuliah dan
NIM harus unik. SKS dan semester harus berupa integer positif. Respons
sukses memakai 200, masukan salah 400, dan ID yang tidak ditemukan 404.

## Contoh hasil cURL

Tangkapan berikut menampilkan keluaran cURL dari server lokal dengan PostgreSQL.

![CRUD mahasiswa](docs/mahasiswa.png)

![CRUD mata kuliah](docs/matakuliah.png)
