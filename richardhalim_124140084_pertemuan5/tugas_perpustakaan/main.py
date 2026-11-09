"""Contoh penggunaan sistem perpustakaan."""

from library import Library
from library_item import Book, Magazine
from member import Member


def cetak_item(items):
    """Tampilkan detail dan status tiap item dalam hasil pencarian."""
    if not items:
        print("Tidak ada item.")
    for item in items:
        status = "Dipinjam" if item.is_dipinjam else "Tersedia"
        print(f"{item.item_id} | {item.get_detail()} | {status}")


def main():
    """Demonstrasikan penambahan, katalog, pencarian, dan peminjaman."""
    perpustakaan = Library()
    anggota = Member("A01", "Richard Halim")
    print("Tambah koleksi")
    for item in (
        Book("B01", "Laut Bercerita", "Leila S. Chudori"),
        Book("B02", "Bumi Manusia", "Pramoedya Ananta Toer"),
        Magazine("M01", "National Geographic", "November"),
        Magazine("M02", "Tempo", "Oktober"),
    ):
        perpustakaan.tambah_item(item)
        print(f"Ditambahkan: {item.item_id} - {item.judul}")

    print("\nKatalog tersedia")
    cetak_item(perpustakaan.daftar_tersedia())
    for kunci in ("laut", "M01", "fisika"):
        print(f"\nCari: {kunci}")
        cetak_item(perpustakaan.cari_item(kunci))

    perpustakaan.pinjam_item("B01", anggota)
    print(f"\n{anggota.nama} meminjam B01.")
    cetak_item(perpustakaan.cari_item("B01"))
    print(f"Katalog tersedia: {len(perpustakaan.daftar_tersedia())} item.")

    perpustakaan.kembalikan_item("B01", anggota)
    print("\nB01 dikembalikan.")
    cetak_item(perpustakaan.cari_item("B01"))


if __name__ == "__main__":
    main()
