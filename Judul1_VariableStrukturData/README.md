# Sistem Rekapitulasi dan Pengecekan Memori Nilai Kuis Mahasiswa
## Deskripsi Singkat
Program ini adalah aplikasi sederhana berbasis teks untuk mencatat nilai kuis mahasiswa, dan untuk membantu memahami bagaimana cara kerja memori di belakang layar. Melalui menu yang disediakan, kita bisa menginputkan nilai untuk lima mahasiswa dan melihar rekap hasil akhirnya. Fitur yang ada bukan hanya untuk menyimpan data, tapi program ini juga bisa menampilkan memory addres (alamat memori) dari array utamanya maupun dari masing-masing indeksnya. 

Program ini menggunakan struktur data array satu dimensi (implementasinya menggunakan list) untuk menampung kelima data nilai tersebut kedalam satu variabel. Program ini menggabungkan looping while agar menu utamanya bisa terus berjalan berulang-ulang, serta perulangan for untuk menelusuri indeks array satu per satu saat proses input data dan pengecekan memori. Agar program aman dan tidak error sama pengguna salah memasukkan huruf, disini diterapkan exception handling atau penanganan error menggunakan blok try except.
## Source Code
<img width="851" height="173" alt="Screenshot 2026-04-28 124013" src="https://github.com/user-attachments/assets/4c17bf36-284a-44ea-97fa-bc1fade6028b" />

Baris 1 adalah fungsi untuk membuat tampilan menu atau perintah yang nantinya akan muncul pada tampilan antarmuka.

Baris 2 dibuat untuk mencetak judul menu ke layar. Karakter \n dipakai untuk membuat baris atau spasi agar lebih rapi.

Baris ke 3 sampai baris ke 7 akan mencetak daftar pilihan yang dapat dipilih oleh pengguna.

<img width="1117" height="794" alt="Screenshot 2026-04-28 124112" src="https://github.com/user-attachments/assets/15797d05-5af2-4aa2-a238-ce284ca8a2cb" />

Baris ke 9 terdapat fungsi utama (def(main)) disini inti logika program akan dijalankan.

Baris ke 10 adalah program membuat list untuk menampung nilai 5 mahasiswa. List ini langsung diisi dengan 5 angka nol. Diibaratkan memesan 5 tempat kosong di memori yang nantinya akan digunakan untuk tempat nilai mahasiswa.

Baris ke 11 membuat variabel bernama running yang nilainya adalah true, jadi selama nilainya true, program akan terus berjalan dalam looping.

Baris ke 12 memulai perulangan utama, selama nilainya masih true akan terus kembali ke menu awal.

Baris ke 13 memanggil fungsi menu yang sudah dibuat pada baris ke 1 untuk ditampilkan ke layar.

Baris ke 14 untuk mencoba menerima input dari pengguna sekaligus penanganan error ketika pengguna tidak sesuai saat memasukkan jenis datanya.

Baris ke 15 untuk menunggu pengguna memasukkan pilihannya





















