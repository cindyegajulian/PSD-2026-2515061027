# Sistem Rekapitulasi dan Pengecekan Memori Nilai Kuis Mahasiswa
## Deskripsi Singkat
Program ini adalah aplikasi sederhana berbasis teks untuk mencatat nilai kuis mahasiswa, dan untuk membantu memahami bagaimana cara kerja memori di belakang layar. Melalui menu yang disediakan, kita bisa menginputkan nilai untuk lima mahasiswa dan melihar rekap hasil akhirnya. Fitur yang ada bukan hanya untuk menyimpan data, tapi program ini juga bisa menampilkan memory addres (alamat memori) dari array utamanya maupun dari masing-masing indeksnya. 

Program ini menggunakan struktur data array satu dimensi (implementasinya menggunakan list) untuk menampung kelima data nilai tersebut kedalam satu variabel. Program ini menggabungkan looping while agar menu utamanya bisa terus berjalan berulang-ulang, serta perulangan for untuk menelusuri indeks array satu per satu saat proses input data dan pengecekan memori. Agar program aman dan tidak error sama pengguna salah memasukkan huruf, disini diterapkan exception handling atau penanganan error menggunakan blok try except.
## Source Code
<img width="851" height="173" alt="Screenshot 2026-04-28 124013" src="https://github.com/user-attachments/assets/4c17bf36-284a-44ea-97fa-bc1fade6028b" />

Baris 1-7 adalah fungsi menu() yang isinya sekumpulan perintah print untuk menampilkan judul program dan pilihan (1-4) ke layar supaya bisa dibaca oleh pengguna.  menu atau perintah yang nantinya akan muncul pada tampilan antarmuka.

<img width="1117" height="794" alt="Screenshot 2026-04-28 124112" src="https://github.com/user-attachments/assets/15797d05-5af2-4aa2-a238-ce284ca8a2cb" />

Baris ke 9-11 membuat fungsi utama (def(main)) sebagai inti program. Lalu membuat list untuk menampung nilai 5 mahasiswa. List ini langsung diisi dengan 5 angka nol. Selanjutnya membuat variabel bernama running yang nilainya adalah true, jadi selama nilainya true, program akan terus berjalan dalam looping.

Baris ke 12 dan 13 memulai perulangan utama, selama nilainya masih true akan terus kembali ke menu awal dan memanggil fungsi menu yang sudah dibuat pada baris ke 1 untuk ditampilkan ke layar.

Baris ke 14-18 untuk mencoba menerima input dari pengguna lewat variabel choice. Lalu pakai blok try except untuk antisipasi jika pengguna salah memberi masukkan (input). Kalau salah, program akan memberi peringatan dan perintah continue yang membuat program kembali ke menu tanpa mengalami error.

Baris 19 dan 20 jika pengguna pilih 1, program bakal nampilin alamat di memori tempat list disimpan, menggunakan bantuan fungsi id().




















