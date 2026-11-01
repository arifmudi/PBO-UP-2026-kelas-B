"""Model domain: alamat penyewa."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Alamat:
    """Objek nilai alamat yang tidak dapat diubah."""

    dusun: str
    desa: str
    kecamatan: str

    def __post_init__(self) -> None:
        if not self.desa.strip():
            raise ValueError("desa tidak boleh kosong")
        if not self.kecamatan.strip():
            raise ValueError("kecamatan tidak boleh kosong")

    def lengkap(self) -> str:
        """Mengembalikan alamat lengkap."""
        return (
            f"Dusun {self.dusun}, "
            f"Desa {self.desa}, "
            f"Kecamatan {self.kecamatan}"
        )

    def singkat(self) -> str:
        """Mengembalikan alamat singkat."""
        return f"{self.desa}, {self.kecamatan}"