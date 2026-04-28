# Sistem Rekapitulasi dan Pengecekan Memori Nilai Kuis Mahasiswa
## Deskripsi Singkat
Program ini adalah aplikasi sederhana berbasis teks untuk mencatat nilai kuis mahasiswa, dan untuk membantu memahami bagaimana cara kerja memori di belakang layar. Melalui menu yang disediakan, kita bisa menginputkan nilai untuk lima mahasiswa dan melihar rekap hasil akhirnya. Fitur yang ada bukan hanya untuk menyimpan data, tapi program ini juga bisa menampilkan memory addres (alamat memori) dari array utamanya maupun dari masing-masing indeksnya. 

Program ini menggunakan struktur data array satu dimensi (implementasinya menggunakan list) untuk menampung kelima data nilai tersebut kedalam satu variabel. Program ini menggabungkan looping while agar menu utamanya bisa terus berjalan berulang-ulang, serta perulangan for untuk menelusuri indeks array satu per satu saat proses input data dan pengecekan memori. Agar program aman dan tidak error sama pengguna salah memasukkan huruf, disini diterapkan exception handling atau penanganan error menggunakan blok try except.
## Source Code
Baris 1 adalah fungsi untuk membuat tampilan menu atau perintah yang nantinya akan muncul pada tampilan antarmuka. Baris 2 dibuat untuk mencetak judul menu ke layar. Karakter \n dipakai untuk membuat baris atau spasi agar lebih rapi.   

