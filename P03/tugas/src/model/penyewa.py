
"""Model domain: petani yang menyewa alat dari UPJA."""

from .alamat import Alamat


class Penyewa:
    """Identitas seorang petani yang menyewa alat dari UPJA."""

    def __init__(
        self,
        nik: str,
        nama: str,
        alamat: Alamat,
        telepon: str = "-",
    ) -> None:
        if len(nik) != 16 or not nik.isdigit():
            raise ValueError("NIK harus terdiri dari 16 angka")

        self._nik = nik
        self._nama = nama
        self._alamat = alamat
        self._telepon = "-"
        self.telepon = telepon

    @property
    def nik(self) -> str:
        """Mengambil NIK penyewa tanpa bisa mengubahnya."""
        return self._nik

    @property
    def alamat(self) -> Alamat:
        """Mengambil alamat penyewa tanpa bisa mengganti objeknya."""
        return self._alamat

    @property
    def telepon(self) -> str:
        """Mengambil nomor telepon penyewa."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        """Memvalidasi nomor telepon sebelum disimpan."""
        if nilai == "-":
            self._telepon = nilai
            return

        angka = nilai.replace("-", "").replace(" ", "")

        if not angka.isdigit() or len(angka) < 10:
            raise ValueError(
                "nomor telepon harus berupa angka dan minimal 10 digit"
            )

        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan baris identitas singkat untuk nota sewa."""
        return f"{self._nama} ({self._nik}) — {self._alamat.singkat()}"

    def kontak(self) -> str:
        """Mengembalikan keterangan cara menghubungi penyewa."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
