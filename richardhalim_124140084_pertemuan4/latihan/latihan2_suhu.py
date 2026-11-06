"""Latihan konversi suhu dari masukan pengguna."""
from math import isfinite


def main():
    """Tanpa parameter; cetak konversi masukan Celsius; kembali None."""
    try:
        celsius = float(input("Suhu Celsius: "))
        if not isfinite(celsius):
            raise ValueError
    except ValueError:
        print("Suhu harus berupa angka yang terbatas.")
        return
    print(f"Fahrenheit: {celsius * 9 / 5 + 32:.2f}")
    print(f"Kelvin    : {celsius + 273.15:.2f}")


if __name__ == "__main__":
    main()
