"""Pengujian untuk kelas Petugas."""

from src.model.petugas import Petugas


def test_identitas_petugas() -> None:
    petugas = Petugas("PT-01", "Azizah", "Admin")
    assert petugas.identitas() == "Azizah (PT-01) - Admin"


def test_kontak_petugas() -> None:
    petugas = Petugas("PT-02", "Nur", "Operator", "081234567890")
    assert petugas.kontak() == "Nur dapat dihubungi di 081234567890"


def test_dua_objek_menyimpan_data_masing_masing() -> None:
    petugas_a = Petugas("PT-03", "Azizah", "Admin")
    petugas_b = Petugas("PT-04", "Nur", "Operator")

    assert petugas_a.identitas() == "Azizah (PT-03) - Admin"
    assert petugas_b.identitas() == "Nur (PT-04) - Operator"