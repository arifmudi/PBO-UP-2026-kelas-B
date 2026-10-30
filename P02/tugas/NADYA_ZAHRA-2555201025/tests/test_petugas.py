"""Pengujian untuk kelas Petugas."""

from src.model.petugas import Petugas


def test_identitas_petugas() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin")
    assert petugas.identitas() == "Andi (PT-01) - Admin"


def test_kontak_petugas() -> None:
    petugas = Petugas("PT-02", "Budi", "Operator", "081234567890")
    assert petugas.kontak() == "Budi dapat dihubungi di 081234567890"


def test_dua_objek_menyimpan_data_masing_masing() -> None:
    petugas_a = Petugas("PT-03", "Siti", "Admin")
    petugas_b = Petugas("PT-04", "Rina", "Operator")

    assert petugas_a.identitas() == "Siti (PT-03) - Admin"
    assert petugas_b.identitas() == "Rina (PT-04) - Operator"