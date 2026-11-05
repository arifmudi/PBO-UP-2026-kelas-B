"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    alamat_budi = Alamat("Dusun Kuok", "Kuok", "Kuok")
    alamat_siti = Alamat("Dusun Salo", "Salo", "Salo")

    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat_budi,
        "0812-3456-7890",
    )
    siti = Penyewa("1406014403950002", "Siti Aminah", alamat_siti)

    traktor = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)
    pompa = AlatTani("PA-01", "Pompa Air 3 Inci", 75000)

    print(budi.identitas())
    print(budi.kontak())
    print(siti.kontak())
    print(traktor.keterangan())
    print(
        f"Sewa traktor 3 hari: Rp{traktor.biaya_sewa(3):,}".replace(",", ".")
    )
    print(
        f"Sewa pompa 5 hari  : Rp{pompa.biaya_sewa(5):,}".replace(",", ".")
    )

    print("\n--- Percobaan menembus penjagaan ---")

    try:
        traktor.tarif_harian = 0
    except ValueError as error:
        print(f"Ditolak (tarif nol): {error}")

    try:
        traktor.tarif_harian = -5000
    except ValueError as error:
        print(f"Ditolak (tarif minus): {error}")

    print(f"Tarif tetap utuh: {traktor.keterangan()}")

if __name__ == "__main__":
    main()