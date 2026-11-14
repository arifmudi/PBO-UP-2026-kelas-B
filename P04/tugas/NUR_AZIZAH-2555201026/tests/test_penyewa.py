"""Pengujian untuk kelas Penyewa."""

import pytest
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def test_inisialisasi_penyewa_valid() -> None:
    alamat = Alamat("Simpang Siabu", "Siabu", "Siabu")
    penyewa = Penyewa("1406012509900001", "Nur Azizah", alamat, "081234567890")
    assert penyewa.nik == "1406012509900001"
    assert penyewa.telepon == "081234567890"


def test_nik_kurang_dari_16_digit_ditolak() -> None:
    alamat = Alamat("Simpang Siabu", "Siabu", "Siabu")
    with pytest.raises(ValueError):
        Penyewa("12345", "Nur Azizah", alamat, "081234567890")


def test_nik_bukan_angka_ditolak() -> None:
    alamat = Alamat("Simpang Siabu", "Siabu", "Siabu")
    with pytest.raises(ValueError):
        Penyewa("140601250990000A", "Nur Azizah", alamat, "081234567890")


def test_telepon_tidak_sah_ditolak() -> None:
    alamat = Alamat("Simpang Siabu", "Siabu", "Siabu")
    penyewa = Penyewa("1406012509900001", "Nur Azizah", alamat, "081234567890")
    with pytest.raises(ValueError):
        penyewa.telepon = "123"  # Terlalu pendek / tidak sah[cite: 9]


def test_telepon_boleh_diubah_secara_sah() -> None:
    alamat = Alamat("Simpang Siabu", "Siabu", "Siabu")
    penyewa = Penyewa("1406012509900001", "Nur Azizah", alamat, "081234567890")
    penyewa.telepon = "089876543210"
    assert penyewa.telepon == "089876543210"


def test_telepon_kosong_menjadi_tanda_strip() -> None:
    alamat = Alamat("Simpang Siabu", "Siabu", "Siabu")
    penyewa = Penyewa("1406012509900001", "Nur Azizah", alamat, "081234567890")
    penyewa.telepon = ""
    assert penyewa.telepon == "-"


def test_metode_identitas() -> None:
    alamat = Alamat("Simpang Siabu", "Siabu", "Siabu")
    penyewa = Penyewa("1406012509900002", "Azizah Nur", alamat)
    hasil = penyewa.identitas()
    assert "Azizah Nur (1406012509900002)" in hasil