"""Model domain: petugas yang melayani penyewaan alat UPJA."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PeriodeTugas:
    """Objek nilai beku untuk periode tugas petugas."""

    mulai: str
    selesai: str

    def __post_init__(self) -> None:
        if not self.mulai.strip() or not self.selesai.strip():
            raise ValueError("periode tugas tidak boleh kosong")


class Petugas:
    """Identitas dan informasi petugas yang melayani penyewaan."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        periode: PeriodeTugas,
        telepon: str = "-",
    ) -> None:
        if not id_petugas.strip():
            raise ValueError("ID petugas tidak boleh kosong")
        self._id_petugas = id_petugas
        self._nama = nama
        self._periode = periode
        self._telepon = "-"
        self.telepon = telepon 

    @property
    def id_petugas(self) -> str:
        """ID petugas melekat pada identitas dan tidak dapat diubah."""
        return self._id_petugas

    @property
    def nama(self) -> str:
        """Nama petugas tidak dapat diubah setelah terdaftar."""
        return self._nama

    @property
    def periode(self) -> PeriodeTugas:
        """Periode tugas sebagai objek nilai beku."""
        return self._periode

    @property
    def telepon(self) -> str:
        """Nomor telepon petugas."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        bersih = nilai.replace("-", "").replace(" ", "")
        if bersih == "" or nilai == "-":
            self._telepon = "-"
            return
        if not bersih.isdigit() or len(bersih) < 10:
            raise ValueError(f"nomor telepon tidak sah, diterima '{nilai}'")
        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan informasi identitas petugas."""
        return f"{self._nama} ({self._id_petugas})"

    def kontak(self) -> str:
        """Mengembalikan informasi kontak petugas."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"