# Sistem Pencatatan Nilai Ujian
## Deskripsi Singkat
Program ini berfungsi membantu guru mencatat dan mengelola nilai ujian siswa secara efisien. Melalui menu sederhana, guru dapat memasukkan nilai, mencari nilai tertentu, melihat pencapaian terendah (Min) dan tertinggi (Max), serta menghitung jumlah siswa dan total keseluruhan nilai untuk keperluan evaluasi seperti menghitung rata-rata kelas.

Program ini menerapkan struktur data Binary Search Tree (BST). Data nilai disusun secara hierarkis: nilai yang lebih kecil ditempatkan di cabang kiri node, dan yang lebih besar di cabang kanan. Pendekatan ini membuat proses penambahan (Insert) dan pencarian (Search) data menjadi sangat cepat. Program ini juga menggunakan Inorder Traversal untuk mencetak seluruh nilai siswa agar otomatis terurut dari yang paling kecil hingga paling besar.

## Source Code 
<img width="397" height="151" alt="image" src="https://github.com/user-attachments/assets/1962cef8-26cc-4d6e-ba45-a909335587e4" />

Baris 1 buat class terlebih dahulu yang nantinya digunakan untuk menyimpan nilai ujian siswa.

Baris 2 fungsi yang akan jalan ketika class baru dibuat, ada dua parameter yaitu self dan key, key adalah nilai ujian yang akan dimasukkan.

Baris 3 variabel untuk menyimpan nilai key atau nilai ujiannya.

Baris 4-5 adalah variabel yang nantinya digunakan untuk menyambungkan ke nilai lain. Left menunjuk ke cabang kiri (untuk nilai ujian yang lebih kecil), dan right menunjuk ke cabang kanan (untuk nilai ujian yang lebih besar). Keduanya sama-sama akan kosong (None) di awal karena belum ada nilai lain yang dihubungkan.

<img width="348" height="90" alt="image" src="https://github.com/user-attachments/assets/ad8d7752-3cce-404d-b931-8f07676bf56c" />

Baris 7 class yang nantinya akan mengelola seluruh node.

Baris 8 fungsi untuk inisialisasi saat sistem mulai berjalan

Baris 9 variabel root atau akar, yang awalnya kosong karena belum ada nilai yang di masukkan.
