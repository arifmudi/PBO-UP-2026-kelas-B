"""Pengujian untuk kelas AlatTani."""

import pytest

from src.model.alat_tani import AlatTani


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_dua_objek_punya_data_sendiri() -> None:
    traktor = AlatTani("TR-01", "Traktor", 150000)
    pompa = AlatTani("PA-01", "Pompa", 75000)
    assert traktor.biaya_sewa(1) != pompa.biaya_sewa(1)


def test_biaya_sewa_satu_hari() -> None:
    alat = AlatTani("PA-01", "Pompa", 75000)
    assert alat.biaya_sewa(1) == 75000


def test_keterangan_alat() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.keterangan() == "[TR-01] Traktor — Rp150.000/hari"


def test_kode_tidak_bisa_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        setattr(alat, "kode", "TR-02")


def test_nama_tidak_bisa_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        setattr(alat, "nama", "Pompa")


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("", "Traktor", 150000)


def test_tarif_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -5000)


def test_tarif_terlalu_tinggi_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 6000000)


def test_tarif_tidak_valid_tidak_mengubah_nilai_lama() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)

    with pytest.raises(ValueError):
        alat.tarif_harian = -5000

    assert alat.tarif_harian == 150000