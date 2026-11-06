"""Soal 1: menghitung BMI dan kategorinya sesuai batas pada modul."""

from math import isfinite


def hitung_bmi(berat, tinggi):
    """Terima berat (kg) dan tinggi (m) positif; kembalikan BMI (float)."""
    if not isfinite(berat) or not isfinite(tinggi):
        raise ValueError("Berat dan tinggi harus berupa angka yang terbatas.")
    if berat <= 0 or tinggi <= 0:
        raise ValueError("Berat dan tinggi harus lebih dari nol.")
    return berat / (tinggi * tinggi)


def kategori_bmi(bmi):
    """Terima BMI positif; kembalikan nama kategori menurut soal praktikum."""
    if not isfinite(bmi) or bmi <= 0:
        raise ValueError("BMI harus berupa angka positif yang terbatas.")
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi < 25:
        return "Berat badan normal"
    elif bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


def baca_positif(label):
    """
    Terima label input; ulangi sampai memperoleh float positif dan
    terbatas.
    """
    while True:
        try:
            nilai = float(input(label))
            if not isfinite(nilai) or nilai <= 0:
                raise ValueError
            return nilai
        except ValueError:
            print("Masukkan angka lebih dari nol, misalnya 65 atau 1.70.")


def main():
    """
    Tanpa parameter; baca masukan dan cetak BMI, tidak mengembalikan
    nilai.
    """
    print("PENGHITUNG BMI")
    print("Richard Halim | 124140084")
    try:
        berat = baca_positif("Berat badan (kg): ")
        tinggi = baca_positif("Tinggi badan (m): ")
    except (EOFError, KeyboardInterrupt):
        print("\nInput dibatalkan.")
        return
    bmi = hitung_bmi(berat, tinggi)
    # Tentukan kategori dari nilai asli, bukan nilai yang sudah dibulatkan.
    print(f"\nBMI      : {bmi:.2f}")
    print(f"Kategori : {kategori_bmi(bmi)}")


if __name__ == "__main__":
    main()
