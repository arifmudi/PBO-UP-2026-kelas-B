"""Pengujian untuk kelas Penyewa."""

import pytest

from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def buat_alamat() -> Alamat:
    return Alamat("Suka Maju", "Bangkinang", "Bangkinang Kota")


def test_identitas_penyewa() -> None:
    penyewa = Penyewa("1234567890123456", "Budi Santoso", buat_alamat())
    assert penyewa.identitas() == (
        "Budi Santoso (1234567890123456) — Bangkinang, Bangkinang Kota"
    )


def test_kontak_dengan_nomor_telepon() -> None:
    penyewa = Penyewa(
        "1234567890123456",
        "Budi Santoso",
        buat_alamat(),
        "081234567890",
    )
    assert penyewa.kontak() == (
        "Budi Santoso dapat dihubungi di 081234567890"
    )


def test_kontak_tanpa_nomor_telepon() -> None:
    penyewa = Penyewa("1234567890123456", "Siti Aminah", buat_alamat())
    assert penyewa.kontak() == (
        "Siti Aminah belum mencantumkan nomor telepon"
    )


def test_nik_penyewa() -> None:
    penyewa = Penyewa("1234567890123456", "Budi", buat_alamat())
    assert penyewa.nik == "1234567890123456"


def test_nik_tidak_bisa_diubah() -> None:
    penyewa = Penyewa("1234567890123456", "Budi", buat_alamat())

    with pytest.raises(AttributeError):
        setattr(penyewa, "nik", "1111111111111111")


def test_nik_kurang_dari_16_digit_ditolak() -> None:
    with pytest.raises(ValueError):
        Penyewa("12345", "Budi", buat_alamat())


def test_nik_mengandung_huruf_ditolak() -> None:
    with pytest.raises(ValueError):
        Penyewa("123456789012345A", "Budi", buat_alamat())


def test_nomor_telepon_bisa_diubah() -> None:
    penyewa = Penyewa("1234567890123456", "Budi", buat_alamat())
    penyewa.telepon = "0821 1234 5678"
    assert penyewa.telepon == "0821 1234 5678"


def test_nomor_telepon_kurang_dari_10_digit_ditolak() -> None:
    with pytest.raises(ValueError):
        Penyewa("1234567890123456", "Budi", buat_alamat(), "08123")


def test_nomor_telepon_mengandung_huruf_ditolak() -> None:
    with pytest.raises(ValueError):
        Penyewa(
            "1234567890123456",
            "Budi",
            buat_alamat(),
            "0812ABC45678",
        )


def test_alamat_tidak_bisa_diganti() -> None:
    penyewa = Penyewa("1234567890123456", "Budi", buat_alamat())

    with pytest.raises(AttributeError):
        setattr(penyewa, "alamat", buat_alamat())