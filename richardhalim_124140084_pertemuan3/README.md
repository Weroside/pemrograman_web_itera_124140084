# Pertemuan 3 — Halaman Profil Saya

**Nama:** Richard Halim  
**NIM:** 124140084  
**Kelas:** RA

## Topik halaman
**Koleksi Game Favorit** — halaman profil sederhana untuk menampilkan beberapa game sebagai data contoh, gambar ilustrasi, tabel informasi, dan formulir ulasan.

Judul, navigasi, dua bagian data utama, kolom tabel, dan kolom formulir mengikuti pola contoh tugas Pertemuan 3 yang tersedia pada repository praktikum mahasiswa lain. Halaman resmi yang ditautkan untuk pertemuan ini tidak berhasil dimuat oleh alat penelusuran pada sesi pengerjaan, jadi README ini tidak mengklaim bahwa semua instruksi resmi sudah terverifikasi.

## Isi halaman
- Navigasi internal: Beranda, Koleksi Game, Tambah Ulasan.
- Bagian Beranda: dua ilustrasi SVG lokal, masing-masing memakai `figure`, `img`, `alt`, dan `figcaption`.
- Tabel Koleksi Game: Judul Game, Tahun Rilis, Genre, Rating Pribadi. Tabel menggunakan `caption`, `thead`, `th scope="col"`, `th scope="row"`, dan empat baris data contoh.
- Form Tambah Ulasan: Judul Game, Tahun Rilis, Rating, dengan label yang terhubung ke input dan validasi dasar.
- Footer identitas: Richard Halim · 124140084.

**Catatan data:** judul dan rating pada tabel adalah data contoh untuk demonstrasi struktur. Ubah sesuai game dan penilaian pribadi sebelum dikumpulkan.

## Struktur folder
```text
richardhalim_124140084_pertemuan3/
├── profil.html
├── gambar-satu.svg
├── gambar-kedua.svg
└── README.md
```

## Cara menjalankan
Tidak memerlukan instalasi atau dependency. Buka `profil.html` langsung di browser, atau gunakan Live Server di VS Code.

## Batasan prototipe
Formulir disediakan untuk memperlihatkan struktur dan validasi HTML. Tanpa backend atau JavaScript, tombol kirim tidak menyimpan ulasan ke database. Perilaku penyimpanan tidak diklaim sebagai bagian dari hasil tugas ini.

## Checklist pemeriksaan
- [x] HTML berbahasa Indonesia dan memiliki title serta viewport.
- [x] Navigasi internal mengarah ke ID bagian yang tersedia.
- [x] Dua gambar lokal memiliki teks alternatif dan keterangan.
- [x] Tabel memiliki caption, thead, header kolom, dan lebih dari tiga baris data.
- [x] Setiap input formulir memiliki label yang terkait dan validasi dasar.
- [x] Identitas Richard Halim dan NIM 124140084 dicantumkan.
- [ ] Cocokkan kembali dengan laman resmi dan worksheet dosen setelah dapat diakses.
