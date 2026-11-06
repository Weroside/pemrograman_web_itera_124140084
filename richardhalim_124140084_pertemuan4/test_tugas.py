"""Pemeriksaan rumus, batas kategori, tabel, dan jalur input CLI."""

import contextlib
import io
import subprocess
import sys
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

import math_operations as operasi
from tugas1_bmi import baca_positif, hitung_bmi, kategori_bmi
from tugas2_nilai_mahasiswa import (
    DATA_MAHASISWA, cari_ekstrem, hitung_nilai_akhir, olah_nilai,
    tentukan_grade,
)


class UjiBMI(unittest.TestCase):
    """Cek perhitungan, kategori batas, dan input yang tidak valid."""

    def test_rumus(self):
        """
        Tanpa parameter; pastikan berat 65 dan tinggi 1.7 menghasilkan
        BMI.
        """
        self.assertAlmostEqual(hitung_bmi(65, 1.7), 22.49134948096886)

    def test_batas_kategori(self):
        """
        Tanpa parameter; cek setiap interval tepat di batas dan di
        bawahnya.
        """
        kasus = [(18.49, "Berat badan kurang"),
                 (18.5, "Berat badan normal"),
                 (24.99, "Berat badan normal"),
                 (25, "Berat badan berlebih"),
                 (29.99, "Berat badan berlebih"), (30, "Obesitas")]
        for bmi, kategori in kasus:
            with self.subTest(bmi=bmi):
                self.assertEqual(kategori_bmi(bmi), kategori)

    def test_input_tidak_valid(self):
        """
        Tanpa parameter; pastikan nol, negatif, NaN, dan infinity
        ditolak.
        """
        for berat, tinggi in [(0, 1.7), (65, 0), (-1, 2),
                              (float("nan"), 2), (65, float("inf"))]:
            with self.subTest(berat=berat, tinggi=tinggi):
                with self.assertRaises(ValueError):
                    hitung_bmi(berat, tinggi)

    def test_input_diulang(self):
        """
        Tanpa parameter; pastikan masukan salah diulang hingga angka
        valid.
        """
        with patch("builtins.input", side_effect=["abc", "0", "nan", "65"]):
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(baca_positif("Berat: "), 65)
        self.assertEqual(output.getvalue().count("Masukkan angka"), 3)


class UjiNilai(unittest.TestCase):
    """Cek bobot, grade, data simulasi, dan pencarian nilai ekstrem."""

    def test_bobot(self):
        """Tanpa parameter; cek formula 30:40:30 dengan nilai yang berbeda."""
        self.assertAlmostEqual(hitung_nilai_akhir(80, 90, 85), 85.5)

    def test_grade(self):
        """Tanpa parameter; cek batas bawah dan atas semua grade A sampai E."""
        for nilai, grade in [(0, "E"), (49.99, "E"), (50, "D"),
                             (59.99, "D"), (60, "C"), (69.99, "C"),
                             (70, "B"), (79.99, "B"), (80, "A"), (100, "A")]:
            with self.subTest(nilai=nilai):
                self.assertEqual(tentukan_grade(nilai), grade)

    def test_data_dan_ekstrem(self):
        """Tanpa parameter; cek minimal lima data, kelengkapan, dan ekstrem."""
        awal = deepcopy(DATA_MAHASISWA)
        self.assertGreaterEqual(len(awal), 5)
        for item in awal:
            self.assertTrue({"nama", "nim", "nilai_uts", "nilai_uas",
                             "nilai_tugas"} <= item.keys())
        hasil = olah_nilai(awal)
        self.assertEqual(awal, DATA_MAHASISWA)
        self.assertEqual([item["grade"] for item in hasil], list("ABCDE"))
        tinggi, rendah = cari_ekstrem(hasil)
        self.assertEqual(tinggi[0]["nama"], "Richard Halim")
        self.assertEqual(rendah[0]["nama"], "Dewi Lestari")

    def test_seri_dan_kosong(self):
        """
        Tanpa parameter; cek semua pemenang seri serta penolakan data
        kosong.
        """
        hasil = olah_nilai([DATA_MAHASISWA[0], DATA_MAHASISWA[0]])
        tinggi, rendah = cari_ekstrem(hasil)
        self.assertEqual(len(tinggi), 2)
        self.assertEqual(len(rendah), 2)
        with self.assertRaises(ValueError):
            cari_ekstrem([])

    def test_nilai_invalid(self):
        """
        Tanpa parameter; cek nilai di luar 0-100 dan nilai nonfinit
        ditolak.
        """
        for nilai in (-1, 101, float("nan"), float("inf")):
            with self.subTest(nilai=nilai):
                with self.assertRaises(ValueError):
                    hitung_nilai_akhir(nilai, 70, 80)
                with self.assertRaises(ValueError):
                    tentukan_grade(nilai)


class UjiModul(unittest.TestCase):
    """Cek seluruh fungsi geometri dan suhu dengan hasil pembanding."""

    def test_geometri(self):
        """Tanpa parameter; cek keenam fungsi geometri dan sisi nol."""
        self.assertEqual(operasi.luas_persegi(4), 16)
        self.assertEqual(operasi.keliling_persegi(4), 16)
        self.assertEqual(operasi.luas_persegi_panjang(8, 3), 24)
        self.assertEqual(operasi.keliling_persegi_panjang(8, 3), 22)
        self.assertAlmostEqual(operasi.luas_lingkaran(7), 153.93791)
        self.assertAlmostEqual(operasi.keliling_lingkaran(7), 43.98226)
        self.assertEqual(operasi.luas_persegi(0), 0)

    def test_suhu(self):
        """Tanpa parameter; cek suhu negatif, titik beku, dan titik didih."""
        for celsius, fahrenheit, kelvin in [(-40, -40, 233.15),
                                            (0, 32, 273.15),
                                            (100, 212, 373.15)]:
            with self.subTest(celsius=celsius):
                self.assertAlmostEqual(
                    operasi.celsius_ke_fahrenheit(celsius), fahrenheit)
                self.assertAlmostEqual(
                    operasi.celsius_ke_kelvin(celsius), kelvin)

    def test_geometri_invalid(self):
        """
        Tanpa parameter; pastikan setiap fungsi menolak ukuran yang
        salah.
        """
        for nilai in (-1, float("nan"), float("inf")):
            for fungsi in (operasi.luas_persegi, operasi.keliling_persegi,
                           operasi.luas_lingkaran, operasi.keliling_lingkaran):
                with self.assertRaises(ValueError):
                    fungsi(nilai)
            for fungsi in (operasi.luas_persegi_panjang,
                           operasi.keliling_persegi_panjang):
                with self.assertRaises(ValueError):
                    fungsi(4, nilai)

    def test_cli(self):
        """
        Tanpa parameter; jalankan ketiga skrip dan periksa hasil
        keluarannya.
        """
        folder = Path(__file__).parent
        for berkas, masukan, potongan in [
            ("tugas1_bmi.py", "65\n1.7\n", "BMI      : 22.49"),
            ("tugas2_nilai_mahasiswa.py", "", "Tertinggi: Richard Halim"),
            ("main.py", "", "373.15 K"),
        ]:
            with self.subTest(berkas=berkas):
                hasil = subprocess.run(
                    [sys.executable, str(folder / berkas)], input=masukan,
                    text=True, capture_output=True, timeout=10,
                )
                self.assertEqual(hasil.returncode, 0, hasil.stderr)
                self.assertIn(potongan, hasil.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
