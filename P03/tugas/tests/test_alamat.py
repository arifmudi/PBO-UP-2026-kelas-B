"""Pengujian untuk kelas Alamat."""

import pytest

from dataclasses import FrozenInstanceError

from src.model.alamat import Alamat


def test_alamat_lengkap() -> None:
    alamat = Alamat("Suka Maju", "Bangkinang", "Bangkinang Kota")
    assert alamat.lengkap() == (
        "Dusun Suka Maju, Desa Bangkinang, Kecamatan Bangkinang Kota"
    )


def test_alamat_singkat() -> None:
    alamat = Alamat("Suka Maju", "Bangkinang", "Bangkinang Kota")
    assert alamat.singkat() == "Bangkinang, Bangkinang Kota"


def test_desa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Suka Maju", "", "Bangkinang Kota")


def test_kecamatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Suka Maju", "Bangkinang", "")


def test_desa_tidak_bisa_diubah() -> None:
    alamat = Alamat("Suka Maju", "Bangkinang", "Bangkinang Kota")

    with pytest.raises(FrozenInstanceError):
        setattr(alamat, "desa", "Kuok")