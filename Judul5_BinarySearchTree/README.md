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

<img width="750" height="320" alt="image" src="https://github.com/user-attachments/assets/42479373-4a0e-4242-88f3-4c724586bd4d" />

Baris 11 fungsi yang digunakan untuk menambahkan nilai baru. 

Baris 12 & 13 jika root kosong, return node(key). Artinya ketika root kosong, belum ada nilai sama sekali, nilai yang pertama masuk akan menempati posisi root.

Baris 14 & 15 ketika nilai key kurang dari root dia akan digeser ke sebelah kiri atau cabang kiri untuk diproses lagi.

Baris 16 & 17, ketika nilai key lebih besar dari root, akan di geser ke subpohon kanan atau akan digeser ke sebelah kanan root

Baris 18 mengembalikan dengan versi yang sudah diperbarui.

Baris 20 & 21 fungsi yang anntinya dipakai di menu. user cukup menginputkan angka  lalu sistem akan memanggil insert.

<img width="674" height="235" alt="image" src="https://github.com/user-attachments/assets/aa259f4c-cc06-4d45-a64c-1be992c1f72b" />

Baris 23 & 25 fungsi untuk mencari node, ketika root kosong akan return false, artinya tidak ada node selanjutnya, karena yang akan pertama kali dicari adalah root

Baris 26 & 27 jika nilai di root sama dengan key, artinya nilai yang dicari sudah ditemukan karena itulah true. 

Baris 28 & 30 jika nilai key kurang dari root artinya nilai yang dicari ada di subpohon kiri karena dia lebih kecil. Nah kalau engga di subpohon kanan berarti dia lebih besar.
