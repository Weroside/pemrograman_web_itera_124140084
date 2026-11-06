"""Latihan while dan break melalui permainan tebak angka."""


def main():
    """Tanpa parameter; minta tebakan sampai tepat atau EOF; kembali None."""
    angka_rahasia = 7
    while True:
        try:
            tebakan = int(input("Tebak angka 1-10: "))
        except ValueError:
            print("Masukkan bilangan bulat.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nPermainan dihentikan.")
            break
        if tebakan < angka_rahasia:
            print("Terlalu kecil!")
        elif tebakan > angka_rahasia:
            print("Terlalu besar!")
        else:
            print("Selamat, tebakan benar!")
            break


if __name__ == "__main__":
    main()
