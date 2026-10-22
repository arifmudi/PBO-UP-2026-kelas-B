KUIS P01
A.	KUIS AWAL (DIKERJAKAN SEBELUM PRAKTIKUM, 15 MENIT)
 
Kuis ini menjembatani dari mata kuliah Algoritma dan Pemrograman. Jawab tanpa membuka catatan.
1.	Apa keluaran potongan kode berikut? Jelaskan mengapa.

Outputnya adalah = 15666
Karena pada awalnya variabel total bernilai 0, lalu perulangan for akan menjumlahkan semua harga yang ada di dalam list, yaitu 15000 + 20000 + 12000 sehingga totalnya menjadi 47000. Setelah itu, total dibagi dengan jumlah data yang ada, yaitu 3. Karena menggunakan operator //, hasil pembagian tidak menampilkan angka desimal, jadi keluarannya adalah 15666.

2.	Apa perbedaan tanda = dan == pada Python?

Tanda = itu digunakan untuk memasukkan nilai ke dalam variabel, misalnya x = 10, artinya variabel x diisi dengan nilai 10. Sedangkan == digunakan untuk membandingkan dua nilai, apakah nilainya sama atau beda. Kalau nilainya sama hasilnya True, kalau beda hasilnya akan menjadi False

3.	Sebutkan dua alasan mengapa kode yang berulang sebaiknya dijadikan fungsi.

1.	Supaya kode tidak ditulis berulang-ulang, karena kalau ada perintah yang sama bisa dibuat dalam satu fungsi dan dipanggil lagi saat dibutuhkan.
2.	Biar kode lebih rapi dan gampang diperbaiki, jadi kalau ada kesalahan atau mau mengubah bagian tertentu, tidak perlu mengubah kode yang sama satu per satu.

4.	Tipe data apa yang tepat untuk menyimpan tarif sewa harian dalam rupiah, dan mengapa bukan yang lain?

Pakai tipe data int karena tarif sewa harian biasanya berupa angka bulat, misalnya 50000. Kalau pakai tipe data str/string, angkanya dianggap teks dan ga bisa langsung dipakai untuk perhitungan. Tipe data float juga bisa, tapi tipe data int itu lebih pas karena tarif rupiah biasanya ga perlu angka koma.

5.	Pada Python, apa akibatnya bila indentasi sebuah baris di dalam fungsi salah?

Kalau indentasi di dalam fungsi salah, program bisa error dan ga jalan. Soalnya di Python jarak baris kode itu penting buat menentukan mana kode yang ada di dalam fungsi. Kalau spasinya berantakan atau ga sesuai, bisa muncul error dan kodenya ga bisa dijalankan dengan benar.

