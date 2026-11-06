"""Soal 3: mencoba seluruh fungsi modul dengan beberapa nilai masukan."""

import math_operations
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin


def main():
    """Tanpa parameter; cetak seluruh contoh geometri/suhu; kembali None."""
    print("MODUL MATEMATIKA | Richard Halim | 124140084")
    print(f"Konstanta PI = {math_operations.PI}")
    print("\nPERSEGI (satuan: cm)")
    for sisi in (4, 7.5):
        math_operations.validasi_ukuran(sisi)
        print(f"Sisi {sisi:g}: "
              f"luas {math_operations.luas_persegi(sisi):.2f} cm^2 | "
              f"keliling {math_operations.keliling_persegi(sisi):.2f} cm")
    print("\nPERSEGI PANJANG (satuan: cm)")
    for panjang, lebar in ((8, 3), (10.5, 4)):
        luas = math_operations.luas_persegi_panjang(panjang, lebar)
        keliling = math_operations.keliling_persegi_panjang(panjang, lebar)
        print(f"Panjang {panjang:g}, lebar {lebar:g}: "
              f"luas {luas:.2f} cm^2 | keliling {keliling:.2f} cm")
    print("\nLINGKARAN (satuan: cm)")
    for jari_jari in (7, 2.5):
        luas = math_operations.luas_lingkaran(jari_jari)
        keliling = math_operations.keliling_lingkaran(jari_jari)
        print(f"Jari-jari {jari_jari:g}: luas {luas:.2f} cm^2 | "
              f"keliling {keliling:.2f} cm")
    print("\nKONVERSI SUHU")
    for celsius in (-40, 0, 25, 100):
        print(f"{celsius:>4} C = {celsius_ke_fahrenheit(celsius):>7.2f} F "
              f"= {celsius_ke_kelvin(celsius):>7.2f} K")


if __name__ == "__main__":
    main()
