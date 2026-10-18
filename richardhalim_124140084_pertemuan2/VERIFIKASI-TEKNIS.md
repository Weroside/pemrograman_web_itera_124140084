# Verifikasi Teknis — PAW Pertemuan 2

**Identitas:** Richard Halim · 124140084 · Kelas RA

## Cakupan proyek
- `01-praktikum-js-nextgen/`: 12 demo JavaScript ES6+ yang dapat dijalankan satu per satu atau bersama-sama.
- `02-tugas-personal-dashboard/`: dashboard tugas, catatan, agenda, pencarian/filter, statistik, tema, ekspor JSON, dan penyimpanan berbasis localStorage.

## Hasil pengujian yang dijalankan
- Dashboard: tambah/edit/hapus tugas, pencarian, tambah catatan, tambah agenda, tema gelap, ekspor JSON, dan lebar viewport ponsel diuji menggunakan Chromium headless.
- Dashboard: 4/4 tes unit Node.js lulus (`node --test tests/dashboard.test.js`).
- Lab ES6+: 12 demo tampil, 12/12 demo selesai, tombol demo asinkron selesai, dan tidak ada exception JavaScript pada pengujian.
- Output demo spread/rest diperbaiki agar hasil fungsi rest parameter terlihat sebagai angka, bukan hilang saat serialisasi JSON.
- Demo class diubah agar menggunakan prioritas bawaan constructor; ini sekaligus memperlihatkan default parameter secara nyata.

## Checklist teknis sementara
Daftar konsep berikut merupakan checklist referensi sekunder yang ditemukan pada dokumentasi mahasiswa lain, bukan salinan atau pengganti instruksi resmi:
- `let` / `const`
- minimal tiga arrow function
- template literals
- destructuring dan spread/rest
- default parameters
- class
- ES modules (import/export)
- array higher-order functions (map/filter/sort/find/reduce)
- Promise dan async/await
- localStorage

Sebagian besar konsep tersebut ditampilkan pada lab ES6+ dan sebagian lagi dipakai pada dashboard.

## Batasan verifikasi
- Halaman resmi materi, tugas, dan format pengumpulan di `praktikum-paw20262027.vercel.app` tidak berhasil dimuat oleh alat penelusuran pada sesi ini. Karena itu, laporan ini **tidak menyatakan seluruh butir resmi telah diverifikasi satu per satu**.
- Uji browser dilakukan dalam harness terisolasi yang memakai source HTML/CSS/JavaScript dari branch `main`; modul digabung untuk render karena navigasi lokal diblokir lingkungan uji. `localStorage` memakai shim in-memory pada uji browser. Tes ini memverifikasi alur UI dan rehidrasi model, tetapi bukan pengujian penyimpanan browser setelah refresh pada origin lokal sesungguhnya.
- Widget cuaca/kutipan diuji pada jalur fallback ketika layanan eksternal tidak tersedia; keberhasilan respons live tidak diuji.

## Cara verifikasi mandiri sebelum dikumpulkan
1. Buka masing-masing folder melalui VS Code Live Server atau jalankan `python -m http.server 8000` dari folder proyek.
2. Di dashboard, jalankan `npm test`.
3. Uji penyimpanan dengan menambah tugas/catatan, refresh browser, lalu pastikan data tetap ada.
4. Jika koneksi tersedia, periksa widget cuaca/kutipan dan tangkap screenshot hasil nyata.
5. Cocokkan kembali semua butir dengan instruksi resmi dosen dan format pengumpulan.
