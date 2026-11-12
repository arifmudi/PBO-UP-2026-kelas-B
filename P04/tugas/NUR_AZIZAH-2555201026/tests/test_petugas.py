"""Pengujian untuk kelas Petugas dan PeriodeTugas."""

import dataclasses
import pytest
from src.model.petugas import Petugas, PeriodeTugas


def test_identitas_petugas() -> None:
    periode = PeriodeTugas("2025", "2026")
    petugas = Petugas("PT-01", "Azizah", periode, "081234567890")
    assert petugas.identitas() == "Azizah (PT-01)"
    assert petugas.id_petugas == "PT-01"


def test_kontak_petugas() -> None:
    periode = PeriodeTugas("2025", "2026")
    petugas = Petugas("PT-02", "Nur", periode, "081234567890")
    assert petugas.kontak() == "Nur dapat dihubungi di 081234567890"


def test_id_petugas_tidak_punya_setter() -> None:
    periode = PeriodeTugas("2025", "2026")
    petugas = Petugas("PT-01", "Azizah", periode)
    with pytest.raises(AttributeError):
        petugas.id_petugas = "PT-99"  # type: ignore[misc]


def test_telepon_tidak_sah_ditolak() -> None:
    periode = PeriodeTugas("2025", "2026")
    petugas = Petugas("PT-01", "Azizah", periode)
    with pytest.raises(ValueError):
        petugas.telepon = "123"


def test_telepon_boleh_diubah_sah() -> None:
    periode = PeriodeTugas("2025", "2026")
    petugas = Petugas("PT-01", "Azizah", periode)
    petugas.telepon = "089876543210"
    assert petugas.telepon == "089876543210"


def test_periode_tugas_tidak_dapat_diubah() -> None:
    p = PeriodeTugas("2025", "2026")
    with pytest.raises(dataclasses.FrozenInstanceError):
        p.mulai = "2024"  # type: ignore[misc]


def test_id_kosong_ditolak() -> None:
    periode = PeriodeTugas("2025", "2026")
    with pytest.raises(ValueError):
        Petugas("", "Azizah", periode)