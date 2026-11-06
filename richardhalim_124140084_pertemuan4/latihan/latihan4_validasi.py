"""Latihan fungsi validator berdasarkan aturan dalam modul."""


def validasi_password(password):
    """Terima string; kembali True jika >= 8 karakter dan ada angka."""
    return len(password) >= 8 and any(huruf.isdigit() for huruf in password)


if __name__ == "__main__":
    for contoh in ("abc", "abcdefgh", "belajar123", "12345678"):
        print(f"{contoh!r}: {validasi_password(contoh)}")
