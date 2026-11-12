import pytest
from src.model.kios import Kios


def test_kios_dibuat_dengan_benar() -> None:
    produk = Kios("BRS", "Beras Anak Daro", 14500, 17000)
    assert produk.kode == "BRS"
    assert produk.nama == "Beras Anak Daro"

def test_harga_wajar_dipanggil_tanpa_objek() -> None:
    assert Kios.harga_jual_wajar(10000, 11500) is True
    assert Kios.harga_jual_wajar(10000, 10500) is False

def test_pencacah_naik_pola_selisih() -> None:
    awal = Kios.jumlah_produk_terdaftar()
    Kios("GLA", "Gula Pasir 1kg", 15000, 17000)
    Kios("MYK", "Minyak Goreng 1L", 14000, 16000)
    assert Kios.jumlah_produk_terdaftar() == awal + 2

def test_konstruktor_dari_baris_csv() -> None:
    produk = Kios.dari_baris_csv("TLR;Telur Ayam 1 Papan;45000;52000")
    assert produk.kode == "TLR"
    assert produk.harga_modal == 45000
    assert produk.harga_jual == 52000

def test_format_keluaran_fstring() -> None:
    produk = Kios("KCG", "Kacang Tanah", 20000, 25000)
    laporan = produk.laporan_terformat()
    assert "Rp20.000" in laporan
    assert "Rp25.000" in laporan

def test_tolak_modal_dibawah_batas_minimum() -> None:
    with pytest.raises(ValueError):
        Kios("KPG", "Kerupuk Mambo", 500, 1000)

def test_tolak_harga_jual_dibawah_margin() -> None:
    with pytest.raises(ValueError):
        Kios("BRS", "Beras Merah", 20000, 21000) 

def test_tolak_baris_csv_kurang_bagian() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("GLA;Gula Pasir;15000") 

def test_tolak_baris_csv_harga_bukan_angka() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("MYK;Minyak Goreng;limabelasribu;20000")

def test_tolak_ubah_kode_karena_readonly() -> None:
    produk = Kios("GND", "Gandum", 10000, 12000)
    with pytest.raises(AttributeError):
        produk.kode = "TGN" # type: ignore[misc]