# Pertemuan 4 — Dasar Pemrograman Python

**Richard Halim · NIM 124140084 · Kelas RA**

Tiga program konsol untuk latihan variabel, percabangan, perulangan, fungsi, list, dictionary, dan modul Python. Seluruh program menggunakan pustaka bawaan Python, sehingga tidak memerlukan `pip install`.

## Menjalankan di VS Code

1. Pasang Python 3.10 atau lebih baru dan ekstensi Python di VS Code.
2. Buka folder `richardhalim_124140084_pertemuan4` melalui **File → Open Folder**.
3. Buka **Terminal → New Terminal** dan cek `python --version`.
4. Jalankan masing-masing program:

```bash
python tugas1_bmi.py
python tugas2_nilai_mahasiswa.py
python main.py
```

Jika menjalankan dari direktori utama repo, masuk dahulu dengan:

```bash
cd richardhalim_124140084_pertemuan4
```

Pada macOS/Linux, gunakan `python3` jika perintah `python` tidak tersedia. Modul `math_operations.py` diimpor oleh `main.py`, sehingga tidak perlu dijalankan sendiri.

## Isi folder

```text
richardhalim_124140084_pertemuan4/
├── .gitignore
├── README.md
├── tugas1_bmi.py
├── tugas2_nilai_mahasiswa.py
├── math_operations.py
├── main.py
├── test_tugas.py
├── docs/
│   ├── soal1-bmi.png
│   ├── soal2-nilai.png
│   ├── soal3-modul.png
│   ├── bmi.txt
│   ├── nilai.txt
│   ├── modul.txt
│   └── hasil-pengujian.txt
└── latihan/
    ├── latihan1.py
    ├── latihan2_suhu.py
    ├── latihan3_tebak.py
    ├── latihan4_validasi.py
    ├── latihan5_kontak.py
    ├── password_gen.py
    └── main.py
```

## Soal 1: Penghitung BMI (30%)

Program membaca berat dalam **kg** dan tinggi dalam **meter**, lalu memanggil `hitung_bmi(berat, tinggi)`. Rumusnya `berat / (tinggi * tinggi)`. `kategori_bmi(bmi)` menggunakan `if-elif-else` untuk kategori berikut:

| BMI | Kategori sesuai modul |
|---|---|
| < 18.5 | Berat badan kurang |
| 18.5 sampai < 25 | Berat badan normal |
| 25 sampai < 30 | Berat badan berlebih |
| >= 30 | Obesitas |

Hasil dicetak dengan f-string dua angka desimal. Penentuan kategori memakai nilai BMI sebelum pembulatan. `baca_positif(label)` mengulang masukan jika teks bukan angka, nol, negatif, NaN, atau tak hingga. Input desimal menggunakan titik, misalnya `1.70`, bukan `170`.

Contoh masukan: berat `65`, tinggi `1.70`. Hasil: **22.49**, kategori **Berat badan normal**. Kategori ini mengikuti ketentuan soal praktikum.

![Hasil eksekusi soal 1](docs/soal1-bmi.png)

## Soal 2: Nilai mahasiswa (40%)

`DATA_MAHASISWA` berisi lima dictionary dengan kunci `nama`, `nim`, `nilai_uts`, `nilai_uas`, dan `nilai_tugas`. Nama serta nilai selain identitas praktikan merupakan **data simulasi**, bukan data akademik sebenarnya.

Alurnya:

1. `hitung_nilai_akhir(uts, uas, tugas)` menerapkan bobot **30% UTS + 40% UAS + 30% tugas**.
2. `tentukan_grade(nilai_akhir)` menentukan A (>= 80), B (>= 70), C (>= 60), D (>= 50), atau E (< 50).
3. `olah_nilai(data_mahasiswa)` menghasilkan rekap baru tanpa mengubah data sumber.
4. `cari_ekstrem(hasil)` mengembalikan daftar mahasiswa bernilai tertinggi dan terendah. Jika seri, semua mahasiswa yang memiliki nilai tersebut ditampilkan.
5. `main()` menampilkan tabel Nama, NIM, UTS, UAS, Tugas, Nilai Akhir, dan Grade menggunakan perataan f-string.

Contoh nilai akhir: 85.50 (A), 75.50 (B), 65.50 (C), 55.50 (D), dan 45.50 (E). Nilai tertinggi milik Richard Halim (85.50); terendah milik Dewi Lestari (45.50). Data kosong untuk pencarian ekstrem dan nilai di luar 0–100 ditolak dengan `ValueError`.

![Hasil eksekusi soal 2](docs/soal2-nilai.png)

## Soal 3: Modul matematika (30%)

`math_operations.py` menyediakan konstanta **PI = 3.14159** dan fungsi berikut:

| Fungsi | Masukan | Hasil |
|---|---|---|
| `luas_persegi` | sisi | sisi pangkat dua |
| `keliling_persegi` | sisi | 4 × sisi |
| `luas_persegi_panjang` | panjang, lebar | panjang × lebar |
| `keliling_persegi_panjang` | panjang, lebar | 2 × (panjang + lebar) |
| `luas_lingkaran` | jari-jari | PI × jari-jari pangkat dua |
| `keliling_lingkaran` | jari-jari | 2 × PI × jari-jari |
| `celsius_ke_fahrenheit` | Celsius | C × 9/5 + 32 |
| `celsius_ke_kelvin` | Celsius | C + 273.15 |
| `validasi_ukuran` | ukuran | None jika valid; ValueError jika tidak |

`main.py` memanggil seluruh fungsi tersebut dengan dua ukuran berbeda untuk setiap bentuk, serta suhu -40, 0, 25, dan 100 Celsius. Program menggunakan dua cara impor:

```python
import math_operations
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin
```

Contoh hasil: persegi sisi 4 memiliki luas 16.00 cm^2 dan keliling 16.00 cm; suhu 25 C menjadi 77.00 F dan 298.15 K. Ukuran geometri harus tidak negatif dan terbatas. Ukuran nol diterima sebagai kasus batas.

![Hasil eksekusi soal 3](docs/soal3-modul.png)

## Latihan mandiri pendamping

Folder `latihan/` berisi enam latihan mandiri pada bagian materi, terpisah dari tiga soal tugas utama. Minat penelitian pada kartu identitas adalah contoh yang dapat disesuaikan.

```bash
python latihan/latihan1.py
python latihan/latihan2_suhu.py
python latihan/latihan3_tebak.py
python latihan/latihan4_validasi.py
python latihan/latihan5_kontak.py
python latihan/main.py
```

Latihan tersebut mencakup print dan kartu identitas, konversi suhu, tebak angka, validator password, katalog kontak, dan generator password acak. Generator memakai `random` dan `string` sesuai latihan; bukan generator untuk kredensial produksi. Kontak hanya disimpan di memori selama program berjalan.

## Pengujian dan bukti eksekusi

```bash
python -m unittest -v
```

Hasil pemeriksaan **6 November 2026: 13 pengujian lulus**. Kasus uji meliputi rumus BMI, batas 18.5/25/30, pengulangan input invalid, bobot nilai, batas seluruh grade, kelengkapan lima data, nilai ekstrem seri, penolakan data kosong, enam fungsi geometri, konversi suhu, input nonfinit, serta eksekusi ketiga program melalui CLI. Bukti rinci ada di [hasil-pengujian.txt](docs/hasil-pengujian.txt).

Ketiga screenshot di atas diambil dari terminal lokal berbasis peramban yang mengeksekusi program Python sebenarnya. Input BMI diberikan melalui stdin (65 dan 1.70). Output teks asli juga disimpan pada `docs/bmi.txt`, `docs/nilai.txt`, dan `docs/modul.txt`. Untuk mengambil screenshot terminal VS Code sendiri, jalankan tiga perintah utama di atas lalu ambil tangkapan layar masing-masing hasil.

Semua fungsi mempunyai docstring yang menjelaskan masukan dan nilai kembaliannya. Penamaan memakai snake_case dan indentasi empat spasi. Pengecekan `pycodestyle` dilakukan untuk konvensi PEP 8. Folder `venv`, `.venv`, dan `__pycache__` diabaikan melalui `.gitignore`.

## Pemeriksaan terhadap ketentuan laman

| Ketentuan | Implementasi / bukti |
|---|---|
| Folder `[NAMA]_[NIM]_pertemuan4` dan nama repo resmi | `richardhalim_124140084_pertemuan4` dalam `pemrograman_web_itera_124140084` |
| Berkas soal 1 sesuai nama, berat/tinggi, rumus BMI | `tugas1_bmi.py`, `hitung_bmi` |
| Empat kategori dengan if-elif-else dan dua desimal | `kategori_bmi`, `main`; `docs/soal1-bmi.png` |
| Minimal lima dictionary dengan lima kunci wajib | `DATA_MAHASISWA` di `tugas2_nilai_mahasiswa.py` |
| Bobot 30:40:30 dan grade A–E | `hitung_nilai_akhir`, `tentukan_grade` |
| Tabel lengkap serta nilai tertinggi/terendah | `main`, `cari_ekstrem`; `docs/soal2-nilai.png` |
| Modul terpisah, luas/keliling tiga bentuk | Enam fungsi geometri di `math_operations.py` |
| Dua konversi suhu dan konstanta | `celsius_ke_fahrenheit`, `celsius_ke_kelvin`, `PI` |
| Semua fungsi dicoba dengan variasi input | `main.py`; `docs/soal3-modul.png` |
| Minimal dua cara impor | `import math_operations` dan `from math_operations import ...` |
| Identitas, alur tiap program, cara menjalankan, screenshot | README ini beserta folder `docs/` |
| Docstring pada setiap fungsi dan PEP 8 | Seluruh berkas Python |
| Abaikan venv dan cache | `.gitignore` |

## Pengumpulan

Acuan diperiksa pada **6 November 2026**: [Modul resmi Pertemuan 4](https://praktikum-paw20262027.vercel.app/pertemuan/4), bagian Tugas Praktikum dan Format Pengumpulan.

1. Pastikan folder ini beserta kode, README, dan bukti eksekusi sudah ada di repo.
2. Pelajari alur dan hasil setiap program sebelum mengumpulkan.
3. Kirim tautan repo dan laporan yang diminta formulir melalui [Submission Kelas RA](https://forms.gle/J1dJrxXPGy1dtSs58).

Deadline **kelas RA: Sabtu, 7 November 2026 pukul 23.59 WIB**. Laman mencantumkan batas kelas RB yang berbeda: 4 November 2026 pukul 23.59 WIB. Pengiriman formulir dilakukan oleh mahasiswa.
