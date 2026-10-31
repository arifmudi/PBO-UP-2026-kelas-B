"""Titik masuk program. Satu-satunya berkas yang boleh mencetak ke layar.""" 
from src.mahasiswa import Mahasiswa

def main() -> None:
    saya = Mahasiswa("Nur Azizah", "2555201026", "Simpang Siabu")   
    print(saya.perkenalan()) 
    
if __name__ == "__main__":    
    main()