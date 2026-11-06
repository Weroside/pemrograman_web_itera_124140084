"""Soal 2: rekap nilai mahasiswa dengan list berisi dictionary."""

from math import isfinite

# Data simulasi untuk latihan, bukan nilai akademik yang sebenarnya.
DATA_MAHASISWA = [
    {"nama": "Richard Halim", "nim": "124140084",
     "nilai_uts": 80, "nilai_uas": 90, "nilai_tugas": 85},
    {"nama": "Andi Pratama", "nim": "124140085",
     "nilai_uts": 70, "nilai_uas": 80, "nilai_tugas": 75},
    {"nama": "Siti Rahma", "nim": "124140086",
     "nilai_uts": 60, "nilai_uas": 70, "nilai_tugas": 65},
    {"nama": "Budi Santoso", "nim": "124140087",
     "nilai_uts": 50, "nilai_uas": 60, "nilai_tugas": 55},
    {"nama": "Dewi Lestari", "nim": "124140088",
     "nilai_uts": 40, "nilai_uas": 50, "nilai_tugas": 45},
]


def hitung_nilai_akhir(nilai_uts, nilai_uas, nilai_tugas):
    """Terima tiga nilai 0-100; kembalikan nilai akhir berbobot 30:40:30."""
    for nilai in (nilai_uts, nilai_uas, nilai_tugas):
        if not isfinite(nilai) or not 0 <= nilai <= 100:
            raise ValueError("Setiap nilai harus berada dalam rentang 0-100.")
    return 0.30 * nilai_uts + 0.40 * nilai_uas + 0.30 * nilai_tugas


def tentukan_grade(nilai_akhir):
    """Terima nilai akhir 0-100; kembalikan grade A, B, C, D, atau E."""
    if not isfinite(nilai_akhir) or not 0 <= nilai_akhir <= 100:
        raise ValueError("Nilai akhir harus berada dalam rentang 0-100.")
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


def olah_nilai(data_mahasiswa):
    """
    Terima list data mahasiswa; kembalikan list hasil tanpa mengubah
    input.
    """
    hasil = []
    for mahasiswa in data_mahasiswa:
        akhir = hitung_nilai_akhir(
            mahasiswa["nilai_uts"], mahasiswa["nilai_uas"],
            mahasiswa["nilai_tugas"],
        )
        hasil.append({**mahasiswa, "nilai_akhir": akhir,
                      "grade": tentukan_grade(akhir)})
    return hasil


def cari_ekstrem(hasil):
    """
    Terima rekap tidak kosong; kembalikan tuple list tertinggi dan
    terendah.
    """
    if not hasil:
        raise ValueError("Data mahasiswa tidak boleh kosong.")
    maksimum = max(item["nilai_akhir"] for item in hasil)
    minimum = min(item["nilai_akhir"] for item in hasil)
    # Tampilkan semua mahasiswa jika nilai tertinggi atau terendah seri.
    tertinggi = [item for item in hasil if item["nilai_akhir"] == maksimum]
    terendah = [item for item in hasil if item["nilai_akhir"] == minimum]
    return tertinggi, terendah


def main():
    """Tanpa parameter; cetak tabel dan nilai ekstrem; kembali None."""
    hasil = olah_nilai(DATA_MAHASISWA)
    print("REKAP NILAI MAHASISWA (DATA SIMULASI)")
    print("Bobot: UTS 30% | UAS 40% | Tugas 30%")
    garis = "-" * 84
    print(garis)
    print(f"{'Nama':<20} {'NIM':<12} {'UTS':>6} {'UAS':>6} "
          f"{'Tugas':>6} {'Nilai Akhir':>12} {'Grade':>7}")
    print(garis)
    for item in hasil:
        print(f"{item['nama']:<20} {item['nim']:<12} "
              f"{item['nilai_uts']:>6.2f} {item['nilai_uas']:>6.2f} "
              f"{item['nilai_tugas']:>6.2f} {item['nilai_akhir']:>12.2f} "
              f"{item['grade']:>7}")
    print(garis)
    tertinggi, terendah = cari_ekstrem(hasil)
    for label, kelompok in (("Tertinggi", tertinggi), ("Terendah", terendah)):
        for item in kelompok:
            print(f"{label}: {item['nama']} ({item['nim']}) | "
                  f"{item['nilai_akhir']:.2f} | Grade {item['grade']}")


if __name__ == "__main__":
    main()
