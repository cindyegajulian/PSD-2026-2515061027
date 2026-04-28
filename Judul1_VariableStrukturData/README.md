# Sistem Rekapitulasi dan Pengecekan Memori Nilai Kuis Mahasiswa
## Deskripsi Singkat
Program ini adalah aplikasi sederhana berbasis teks untuk mencatat nilai kuis mahasiswa, dan untuk membantu memahami bagaimana cara kerja memori di belakang layar. Melalui menu yang disediakan, kita bisa menginputkan nilai untuk lima mahasiswa dan melihar rekap hasil akhirnya. Fitur yang ada bukan hanya untuk menyimpan data, tapi program ini juga bisa menampilkan memory addres (alamat memori) dari array utamanya maupun dari masing-masing indeksnya. 

Program ini menggunakan struktur data array satu dimensi (implementasinya menggunakan list) untuk menampung kelima data nilai tersebut kedalam satu variabel. Program ini menggabungkan looping while agar menu utamanya bisa terus berjalan berulang-ulang, serta perulangan for untuk menelusuri indeks array satu per satu saat proses input data dan pengecekan memori. Agar program aman dan tidak error sama pengguna salah memasukkan huruf, disini diterapkan exception handling atau penanganan error menggunakan blok try except.
## Source Code
### Bagian 1
Baris 1 adalah fungsi untuk membuat tampilan menu atau perintah yang nantinya akan muncul pada tampilan antarmuka. Baris 2 dibuat untuk mencetak judul menu ke layar. Karakter \n dipakai untuk membuat baris atau spasi agar lebih rapi. Baris ke 3 sampai baris ke 7 akan mencetak daftar pilihan yang dapat dipilih oleh pengguna.
### Bagian 2
Pada baris ke 9 terdapat fungsi utama (def(main)) disini inti logika program akan dijalankan.  
Baris ke 10 adalah program membuat list untuk menampung nilai 5 mahasiswa. List ini langsung diisi dengan 5 angka nol. Diibaratkan memesan 5 tempat kosong di memori yang nantinya akan digunakan untuk tempat nilai mahasiswa.
















