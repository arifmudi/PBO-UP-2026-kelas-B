"""Pengujian untuk kelas AlatTani dan Alamat."""

import dataclasses
import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_dua_objek_punya_data_sendiri() -> None:
    a = AlatTani("TR-01", "Traktor", 150000)
    b = AlatTani("PA-01", "Pompa", 75000)
    assert a.biaya_sewa(1) != b.biaya_sewa(1)


def test_tarif_minus_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -5000)


def test_tarif_minus_ditolak_lewat_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = -5000
    assert alat.tarif_harian == 150000  # Nilai lama tetap utuh


def test_kode_tidak_punya_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-99"  # type: ignore[misc]


def test_alamat_tidak_dapat_diubah() -> None:
    a = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(dataclasses.FrozenInstanceError):
        a.desa = "Salo"  # type: ignore[misc]

def test_denda_keterlambatan() -> None:
    alat = AlatTani("TR-02", "Traktor Besar", 100000)
    assert alat.denda_keterlambatan(3) == 30000


def test_denda_keterlambatan_minus_error() -> None:
    alat = AlatTani("TR-02", "Traktor Besar", 100000)
    with pytest.raises(ValueError):
        alat.denda_keterlambatan(-1)


def test_dari_baris_csv_valid() -> None:
    baris = "TR-03; Traktor Mini; 200000"
    alat = AlatTani.dari_baris_csv(baris)
    assert alat.kode == "TR-03"
    assert alat.nama == "Traktor Mini"
    assert alat.tarif_harian == 200000


def test_dari_baris_csv_format_salah() -> None:
    # Format salah karena kurang dari 3 bagian
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("TR-03; Traktor Mini")


def test_tarif_wajar() -> None:
    assert AlatTani.tarif_wajar(50000) is True
    assert AlatTani.tarif_wajar(5000) is False