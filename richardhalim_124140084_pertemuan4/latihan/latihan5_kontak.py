"""Latihan dictionary kontak, pencarian get(), dan menu sederhana."""


def main():
    """Tanpa parameter; jalankan menu kontak di memori; kembali None."""
    kontak = {}
    while True:
        print("\n1. Tambah kontak | 2. Cari | 3. Tampilkan | 0. Keluar")
        try:
            pilihan = input("Pilihan: ").strip()
            if pilihan == "0":
                break
            if pilihan == "1":
                nama = input("Nama: ").strip()
                nomor = input("Nomor telepon: ").strip()
                if not nama or not nomor:
                    print("Nama dan nomor tidak boleh kosong.")
                    continue
                kontak[nama] = nomor
                print("Kontak tersimpan.")
            elif pilihan == "2":
                nama = input("Nama yang dicari: ").strip()
                print(kontak.get(nama, "Kontak tidak ditemukan."))
            elif pilihan == "3":
                if not kontak:
                    print("Belum ada kontak.")
                for nama, nomor in kontak.items():
                    print(f"{nama}: {nomor}")
            else:
                print("Pilihan tidak tersedia.")
        except (EOFError, KeyboardInterrupt):
            print("\nSelesai.")
            break


if __name__ == "__main__":
    main()
