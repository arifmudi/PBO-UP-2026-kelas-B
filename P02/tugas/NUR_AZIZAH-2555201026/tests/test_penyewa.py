"""Pengujian untuk kelas Penyewa."""

from src.model.penyewa import Penyewa

def test_inisialisasi_penyewa() -> None:
    penyewa = Penyewa("3201123456780001", "Nur Azizah", "Simpang Siabu", "08123456789")
    assert penyewa._nik == "3201123456780001"
    assert penyewa._nama == "Nur Azizah"
    assert penyewa._desa == "Simpang Siabu"
    assert penyewa._telepon == "08123456789"

def test_metode_identitas() -> None:
    penyewa = Penyewa("3201123456780002", "Azizah Nur", "Salo")
    hasil = penyewa.identitas()
    assert hasil == "Azizah Nur (3201123456780002) — Desa Salo"

def test_metode_kontak_dengan_telepon() -> None:
    penyewa = Penyewa("3201123456780003", "Joko Widodo", "Sukatani", "08987654321")
    hasil = penyewa.kontak()
    assert hasil == "Joko Widodo dapat dihubungi di 08987654321"

def test_metode_kontak_tanpa_telepon() -> None:
    penyewa = Penyewa("3201123456780004", "Ani Yudhoyono", "Sukadamai")
    hasil = penyewa.kontak()
    assert hasil == "Ani Yudhoyono belum mencantumkan nomor telepon"