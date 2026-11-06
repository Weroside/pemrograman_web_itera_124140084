"""Soal 3: fungsi geometri dan konversi suhu, tanpa input saat diimpor."""

from math import isfinite

PI = 3.14159


def validasi_ukuran(ukuran):
    """Terima ukuran; kembalikan None atau tolak ukuran negatif/nonfinit."""
    if not isfinite(ukuran) or ukuran < 0:
        raise ValueError(
            "Ukuran harus berupa angka terbatas dan tidak negatif.")


def luas_persegi(sisi):
    """Terima sisi >= 0; kembalikan luas persegi dalam satuan kuadrat."""
    validasi_ukuran(sisi)
    return sisi ** 2


def keliling_persegi(sisi):
    """Terima sisi >= 0; kembalikan keliling persegi dalam satuan panjang."""
    validasi_ukuran(sisi)
    return 4 * sisi


def luas_persegi_panjang(panjang, lebar):
    """Terima panjang dan lebar >= 0; kembalikan luas persegi panjang."""
    validasi_ukuran(panjang)
    validasi_ukuran(lebar)
    return panjang * lebar


def keliling_persegi_panjang(panjang, lebar):
    """Terima panjang dan lebar >= 0; kembalikan keliling persegi panjang."""
    validasi_ukuran(panjang)
    validasi_ukuran(lebar)
    return 2 * (panjang + lebar)


def luas_lingkaran(jari_jari):
    """
    Terima jari-jari >= 0; kembalikan luas lingkaran memakai konstanta
    PI.
    """
    validasi_ukuran(jari_jari)
    return PI * jari_jari ** 2


def keliling_lingkaran(jari_jari):
    """Terima jari-jari >= 0; kembalikan keliling lingkaran dengan PI."""
    validasi_ukuran(jari_jari)
    return 2 * PI * jari_jari


def celsius_ke_fahrenheit(celsius):
    """Terima suhu Celsius terbatas; kembalikan suhu dalam Fahrenheit."""
    if not isfinite(celsius):
        raise ValueError("Suhu harus berupa angka yang terbatas.")
    return celsius * 9 / 5 + 32


def celsius_ke_kelvin(celsius):
    """Terima suhu Celsius terbatas; kembalikan suhu dalam Kelvin."""
    if not isfinite(celsius):
        raise ValueError("Suhu harus berupa angka yang terbatas.")
    return celsius + 273.15
