# Pertemuan 1 — Mini POS dan Dasar JavaScript

**Nama:** Richard Halim  
**NIM:** 124140084  
**Kelas praktikum:** RA

Folder ini mengumpulkan materi dan tugas Pertemuan 1 yang sebelumnya berada di root repository. Konten Mini POS, file JavaScript/CSS, empat latihan, dan screenshot lama dipindahkan tanpa menghapus isinya.

## A. Mini POS Kasir & Keranjang Belanja

Aplikasi kasir sederhana untuk simulasi toko/kantin kampus.

### Fitur
- Validasi nama barang wajib diisi dan minimal 3 karakter.
- Validasi harga positif minimal Rp500 dan kuantitas bilangan bulat minimal 1.
- Perhitungan subtotal, total belanja, diskon 10% untuk total minimal Rp50.000, total akhir, uang bayar, dan kembalian.
- Menambah dan menghapus barang pada keranjang serta reset transaksi.
- Penyimpanan keranjang menggunakan `localStorage` dan JSON.

### Menjalankan
Buka [Mini POS Kasir](./index.html) melalui Live Server di VS Code, atau jalankan server lokal dari folder ini dengan `python -m http.server 8000`.

### Screenshot yang sudah tersedia
- [Form input barang](./screenshots/screenshot_3.png)
- [Validasi error](./screenshots/screenshot_1.png)
- [Hasil perhitungan dan pembayaran](./screenshots/screenshot_2.png)

## B. Latihan modul JavaScript

- [Latihan 1 — JavaScript dasar dan kondisional](./modul/latihan_1_javascript_dasar.html)
- [Latihan 2 — Function dan loop](./modul/latihan_2_function_loop.html)
- [Latihan 3 — Array dan CRUD mahasiswa](./modul/latihan_3_array_crud_mahasiswa.html)
- [Latihan 4 — DOM, LocalStorage, dan Todo](./modul/latihan_4_dom_localstorage_todo.html)

## Teknologi
HTML5, CSS3, JavaScript, DOM, dan LocalStorage.
