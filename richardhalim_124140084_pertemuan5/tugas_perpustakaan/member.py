"""Data anggota perpustakaan."""


class Member:
    """Menyimpan identitas anggota yang meminjam item."""

    def __init__(self, member_id, nama):
        self.__id = member_id
        self.__nama = nama

    @property
    def member_id(self):
        """Kembalikan ID anggota."""
        return self.__id

    @property
    def nama(self):
        """Kembalikan nama anggota."""
        return self.__nama
