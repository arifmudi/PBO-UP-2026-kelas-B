
class Dompet:
    """Contoh class untuk memahami name mangling."""

    def __init__(self, saldo: int) -> None:
        self.__saldo = saldo

    def lihat_saldo(self) -> int:
        return self.__saldo


dompet = Dompet(100000)

print("Saldo awal:", dompet.lihat_saldo())

try:
    print(dompet.__saldo)
except AttributeError:
    print("Akses langsung ditolak")

dompet._Dompet__saldo = -1

print("Saldo setelah diakses:", dompet.lihat_saldo())
