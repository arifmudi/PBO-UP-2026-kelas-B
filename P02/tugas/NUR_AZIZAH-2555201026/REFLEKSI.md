# Refleksi Praktikum Pemrograman Berorientasi Objek (PBO)

## 1. Apa Saja yang Telah Saya Pelajari

Selama praktikum PBO Pertemuan 1 dan 2, beberapa hal penting yang berhasil saya pelajari meliputi:

### A. Konsep Dasar PBO & Tiga Gerbang Mutu
- **Prosedural vs PBO:** Kalau prosedural cuma fokus jalanin fungsi berurutan, kalau PBO itu ngebungkus data (atribut) dan perilaku (method) jadi satu kesatuan di dalam objek.
- **Tiga Gerbang Mutu:** Biar kode kita gak asal jalan tapi bener-bener rapi, wajib lolos:
  1. `periksa_pbo.py`: Buat ngecek aturan PBO, enkapsulasi, dan larangan pake `print` sembarangan di domain.
  2. `mypy`: Buat ngecek tipe data (*type annotations*) biar aman dari error tipe.
  3. `pytest`: Buat ngetes fungsi-fungsi kode secara otomatis.

### B. Pemodelan Kelas & Objek (Studi Kasus UPJA)
- **Bikin Kelas & Enkapsulasi:** Belajar pake konstruktor `__init__` dan bikin atribut privat/protected pake awalan garis bawah (`_`).
- **Parameter Default:** Belajar cara ngasih nilai bawaan di parameter (misalnya `telepon: str = "-"`) biar lebih fleksibel.
- **Prinsip "Beri Perintah, Jangan Bertanya":** Objek disuruh kerja lewat method (misal `biaya_sewa()` atau `identitas()`), bukan malah data di dalam objek yang dibongkar paksa dari luar.
- **Kemandirian Objek:** Buktiin sendiri kalau objek-objek walau dari cetakan kelas yang sama, tetap punya data masing-masing yang terpisah.

---

## 2. Kendala yang Dihadapi dan Solusinya

Berikut beberapa kendala yang sempat bikin pusing selama praktikum beserta cara atasinya:

1. **Lupa Aktifin Virtual Environment (`.venv`)**
   - **Kendala:** Pas buka terminal baru, `pytest` atau `mypy` selalu gagal dan dibilang gak ketemu.
   - **Solusi:** Selalu aktifin `.venv` dulu (`.venv\Scripts\activate`) di awal sebelum ngetik perintah apa-apa.

2. **Kena `TypeError` karena Lupa `self`**
   - **Kendala:** Pas manggil fungsi `alat.biaya_sewa(3)`, malah muncul error `takes 1 positional argument but 2 were given`.
   - **Solusi:** Ingat-ingat lagi kalau setiap method di Python wajib naruh `self` di parameter pertamanya.

3. **Atribut Gampang Diubah Orang Luar (Bypass Enkapsulasi)**
   - **Kendala:** Heran kenapa atribut kayak `alat._tarif_harian = -5000` bisa diubah seenaknya dari luar tanpa ada peringatan dari Python.
   - **Solusi:** Sadar kalau garis bawah (`_`) di Python itu cuman konvensi/kesepakatan doang, makanya butuh trik pengaman lanjutan kayak `@property` nanti.

4. **Ditolak Gerbang Gara-gara "Kode Berjalan di Tingkat Modul"**
   - **Kendala:** Program udah bener dan jalan di komputer, tapi tetep ditolak gerbang pertama.
   - **Solusi:** Ternyata gara-gara ada perintah `print` atau eksekusi kode di luar fungsi/kelas. Semuanya harus dipindahin ke dalam fungsi `main()` yang dilindungi `if __name__ == "__main__":`.