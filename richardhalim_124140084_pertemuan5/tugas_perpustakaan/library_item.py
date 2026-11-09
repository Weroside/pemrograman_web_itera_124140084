"""Jenis item yang dapat dicatat di perpustakaan."""

from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Menyimpan identitas dan status peminjaman setiap item."""

    def __init__(self, item_id, judul):
        self.__id = item_id.strip()
        self._judul = judul.strip()
        if not self.__id or not self._judul:
            raise ValueError("ID dan judul harus diisi.")
        self.__peminjam = None

    @property
    def item_id(self):
        """Kembalikan ID tetap item."""
        return self.__id

    @property
    def judul(self):
        """Kembalikan judul item."""
        return self._judul

    @property
    def is_dipinjam(self):
        """Tunjukkan apakah item sedang dipinjam."""
        return self.__peminjam is not None

    def pinjam(self, anggota):
        """Catat anggota sebagai peminjam jika item tersedia."""
        if self.is_dipinjam:
            raise ValueError("Item sedang dipinjam.")
        self.__peminjam = anggota

    def kembalikan(self, anggota):
        """Kembalikan item yang dipinjam oleh anggota yang sama."""
        if not self.is_dipinjam or self.__peminjam is not anggota:
            raise ValueError("Item tidak dipinjam oleh anggota ini.")
        self.__peminjam = None

    @abstractmethod
    def get_detail(self):
        """Kembalikan deskripsi yang sesuai dengan jenis item."""


class Book(LibraryItem):
    """Buku memiliki informasi penulis."""

    def __init__(self, item_id, judul, penulis):
        super().__init__(item_id, judul)
        self.__penulis = penulis

    def get_detail(self):
        """Kembalikan deskripsi buku dan penulisnya."""
        return f"Buku | {self.judul} - {self.__penulis}"


class Magazine(LibraryItem):
    """Majalah memiliki nomor edisi."""

    def __init__(self, item_id, judul, edisi):
        super().__init__(item_id, judul)
        self.__edisi = edisi

    def get_detail(self):
        """Kembalikan deskripsi majalah dan edisinya."""
        return f"Majalah | {self.judul} - edisi {self.__edisi}"
