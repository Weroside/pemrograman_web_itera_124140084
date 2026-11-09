"""Pengelolaan koleksi perpustakaan."""

from library_item import LibraryItem


class Library:
    """Menambah, menelusuri, dan mengelola peminjaman koleksi."""

    def __init__(self):
        self.__koleksi = {}

    def tambah_item(self, item):
        """Simpan LibraryItem baru dengan ID unik."""
        if not isinstance(item, LibraryItem):
            raise TypeError("Koleksi hanya menerima LibraryItem.")
        kunci = item.item_id.casefold()
        if kunci in self.__koleksi:
            raise ValueError("ID item sudah ada.")
        self.__koleksi[kunci] = item

    def daftar_tersedia(self):
        """Kembalikan tuple item yang belum dipinjam."""
        return tuple(
            item for item in self.__koleksi.values()
            if not item.is_dipinjam
        )

    def cari_item(self, kata_kunci):
        """Cari ID tepat atau potongan judul tanpa membedakan kapital."""
        kunci = kata_kunci.strip().casefold()
        if not kunci:
            return ()
        if kunci in self.__koleksi:
            return (self.__koleksi[kunci],)
        return tuple(
            item for item in self.__koleksi.values()
            if kunci in item.judul.casefold()
        )

    def _ambil_item(self, item_id):
        """Ambil item menurut ID tepat atau laporkan bahwa ID tidak ada."""
        item = self.__koleksi.get(item_id.strip().casefold())
        if item is None:
            raise ValueError(f"ID {item_id} tidak ditemukan.")
        return item

    def pinjam_item(self, item_id, anggota):
        """Pinjamkan item berdasarkan ID kepada anggota."""
        self._ambil_item(item_id).pinjam(anggota)

    def kembalikan_item(self, item_id, anggota):
        """Proses pengembalian item oleh anggota yang meminjamnya."""
        self._ambil_item(item_id).kembalikan(anggota)
