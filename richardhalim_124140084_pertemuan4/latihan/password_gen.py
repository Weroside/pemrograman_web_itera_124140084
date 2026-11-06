"""Latihan modul random dan string, sesuai contoh pada materi."""
import random
import string


def buat_password_acak(panjang=8):
    """Terima panjang bulat positif (default 8); kembali string acak."""
    if (not isinstance(panjang, int)
            or isinstance(panjang, bool) or panjang < 1):
        raise ValueError("Panjang harus berupa bilangan bulat positif.")
    karakter = string.ascii_letters + string.digits
    return "".join(random.choice(karakter) for _ in range(panjang))
