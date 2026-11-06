"""Pemanggil modul generator password untuk latihan nomor 6."""
from password_gen import buat_password_acak

if __name__ == "__main__":
    for panjang in (8, 12, 16):
        print(f"Panjang {panjang}: {buat_password_acak(panjang)}")
