from typing import Final

class Kios:
    """Satu unit produk pertanian yang dijual di Kios UMKM Bangkinang."""
    
    MARGIN_MINIMUM_PERSEN: Final[int] = 10
    HARGA_MODAL_MINIMUM: Final[int] = 1_000
    PEMISAH_BARIS: Final[str] = ";"
    
    _jumlah_produk_terdaftar: int = 0
    
    def __init__(self, kode: str, nama: str, harga_modal: int, harga_jual: int) -> None:
        if not kode.strip():
            raise ValueError("kode produk tidak boleh kosong")
        
        self._kode = kode
        self._nama = nama
        self.harga_modal = harga_modal
        self.harga_jual = harga_jual
        
        Kios._jumlah_produk_terdaftar += 1
        
    @property
    def kode(self) -> str:
        """Kode produk, bersifat baca-saja."""
        return self._kode
        
    @property
    def nama(self) -> str:
        """Nama produk, bersifat baca-saja."""
        return self._nama
        
    @property
    def harga_modal(self) -> int:
        return self._harga_modal
        
    @harga_modal.setter
    def harga_modal(self, nilai: int) -> None:
        if nilai < Kios.HARGA_MODAL_MINIMUM:
            raise ValueError(f"harga modal minimal {Kios.HARGA_MODAL_MINIMUM}, diterima {nilai}")
        self._harga_modal = nilai
        
    @property
    def harga_jual(self) -> int:
        return self._harga_jual
        
    @harga_jual.setter
    def harga_jual(self, nilai: int) -> None:
        if not Kios.harga_jual_wajar(self.harga_modal, nilai):
            raise ValueError(f"harga jual {nilai} terlalu rendah untuk modal {self.harga_modal} (margin min {Kios.MARGIN_MINIMUM_PERSEN}%)")
        self._harga_jual = nilai

    @staticmethod
    def harga_jual_wajar(modal: int, jual: int) -> bool:
        """Memeriksa kewajaran harga jual berdasarkan margin minimum kelas."""
        untung_minimum = modal * Kios.MARGIN_MINIMUM_PERSEN // 100
        return jual >= (modal + untung_minimum)
        
    @classmethod
    def jumlah_produk_terdaftar(cls) -> int:
        """Banyaknya produk yang sudah didaftarkan ke sistem."""
        return cls._jumlah_produk_terdaftar
        
    @classmethod
    def dari_baris_csv(cls, baris: str) -> "Kios":
        """Membuat produk dari satu baris pendataan teks."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)
        if len(bagian) != 4:
            raise ValueError(f"baris harus berisi 4 bagian, diterima {len(bagian)}")
            
        kode, nama, modal, jual = bagian
        if not modal.strip().isdigit() or not jual.strip().isdigit():
            raise ValueError("harga modal dan jual harus berupa angka")
            
        return cls(kode.strip(), nama.strip(), int(modal), int(jual))
        
    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Mengubah angka menjadi string format rupiah."""
        return "Rp" + f"{nilai:,}".replace(",", ".")
        
    def laporan_terformat(self) -> str:
        """5. Pemformatan: Keluaran dengan perataan f-string agar rapi."""
        modal_str = Kios.format_rupiah(self.harga_modal)
        jual_str = Kios.format_rupiah(self.harga_jual)
        return f"[{self.kode:^5}] {self.nama:<20} Modal: {modal_str:>12} | Jual: {jual_str:>12}"