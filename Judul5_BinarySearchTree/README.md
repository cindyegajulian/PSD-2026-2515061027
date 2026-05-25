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

Baris 20 & 21 fungsi utama agar menu langsung memanggil fungsi insert dan memulai dari self.root

<img width="674" height="235" alt="image" src="https://github.com/user-attachments/assets/aa259f4c-cc06-4d45-a64c-1be992c1f72b" />

Baris 23 & 25 fungsi untuk mencari node, ketika root kosong akan return false, artinya tidak ada node selanjutnya, karena yang akan pertama kali dicari adalah root

Baris 26 & 27 jika nilai di root sama dengan key, artinya nilai yang dicari sudah ditemukan karena itulah true. 

Baris 28-30 jika nilai key kurang dari root artinya nilai yang dicari ada di subpohon kiri karena dia lebih kecil. Nah kalau dia lebih besar dari root maka yang dicari ada di subpohon kanan.

<img width="625" height="62" alt="image" src="https://github.com/user-attachments/assets/dbf283e3-0198-48c4-a3c1-7f595d6d3945" />

Baris 32 & 33 sama seperti insert, ini adalah fungsi utama agar menu langsung mencari mulai dari self.root

<img width="452" height="179" alt="Screenshot 2026-05-25 082530" src="https://github.com/user-attachments/assets/774dffd2-6395-4ff5-a2c4-16a288b867e6" />

Baris 35-39 Baris dengan fungsi inorder, jika root kosong return none. Ketika root ada isinya program akan lanjut menelusuri kiri  dulu, (root.left). Saat sebelah kiri selesai ditelusuri program akan mencetak nilai ujian yang ada diposisi root.key lalu end= " " agar angka yang dicetak berbaris rapi ke samping bukan ke bawah. Setelah proses cetak selesai, yang terakhir dilakukan adalah mengecek sebelah kanan (root.right). Mudahnya dia akan jalan dari kiri - root - kanan. 

<img width="456" height="177" alt="image" src="https://github.com/user-attachments/assets/86bda090-66a9-4cbd-9e92-882cbea744be" />

Baris 42-47 baris dengan fungsi preorder, sama seperti inorder, bedanya preorder akan mencetak nilai rootnya terlebih dahulu (print(root.key, end= " ")) baru  setelahnya akan menelusuri sebelah kiri dan terakhir ke kanan. Nah preorder jalan dari root -  kiri - kanan.

<img width="469" height="183" alt="image" src="https://github.com/user-attachments/assets/57542a3c-e38f-4066-97fd-5f1082f80f27" />

Baris 49-54 baris dengan fungsi postorder, sama dengann inorder dan preorder, yang membedakan adalah, postorder mulai menelusuri dari sebelah kiri terlebih dahuku, lalu lanjut ke kanan, setelah baru ke root. Baru setelahnya akan mencetak  nilainya. Alur jalannya  kiri - kanan - root.

<img width="529" height="204" alt="image" src="https://github.com/user-attachments/assets/216cfbf9-d2f7-4f8c-b746-1873d9158223" />

Baris 56-62 Baris dengaan fungsi find_min, awal mencari dari root terlebih dahulu, jika root kosong akan return -1. Buat variabel current untuk menyimpan root. Perulangan ketika sebelah kiri belum kosong program akan terus berjalan ke kiri, karena yang dicari adalah angka terkecil (min). Return current.key artinya program sudah tidak menemukan lagi cabang kiri, yang ditemukan saat itu lah nilai terkecilnya.

<img width="546" height="207" alt="image" src="https://github.com/user-attachments/assets/3c832b8d-388b-44d4-b3d9-424e0d4d8818" />

Baris 64-70 baris dengan fungsi find_max, ini kebalikan dari yang sebelumnya logikanya sama hanya beda ketika min akan mencari ke kiri, nah max akan terus mencari ke kanan sssampai menemukan yang paling ujung, karena mencari nilai  terbesar.

<img width="981" height="125" alt="image" src="https://github.com/user-attachments/assets/a20df20f-401c-4b73-8483-6631c55ecbf7" />

Baris 72-75 Baris dengan fungsi count_nodes untuk menghitung berapa banyak node yang ada, kalau di program itu menghitung berapa banyak siswa yang mengumpulkan nilai ujian. Pertama akan cek root, ketika dia kosong akan return 0 artinya tidak ada node yang bisa dihitung karena kosong. Nah kalau ga kosong akan lanjut ke perhitungan berapa banyak node yang ada, 1 untuk root lalu ditambah dengan node kiri dan node kanan.

<img width="1018" height="122" alt="image" src="https://github.com/user-attachments/assets/a032b81a-0574-4371-aba6-b6fcce2177c4" />

Baris 77-80 fungsi sum_nodes untuk  menjumlahkan semua isi dari node. Seperti sebelumnya, ketika root kosong akan return 0 tetapi jika root tidak kosong akan lanjut ke perhitungan jumlah dari node dengan menambahkan nilai di root lalu tambahkan dengan hasil penjumlahan sebelah kiri lalu sebelah kanan.


<img width="920" height="431" alt="image" src="https://github.com/user-attachments/assets/2d52e5b2-be97-4e1e-94a2-07b2c9dabe77" />

Baris 82-96 fungsi main yang akan dijalankan nanti, menyimpan class BSTDasar yang logika diawal tadi di variabel bst untuk mengaktifkan programnya. While pilih != 10 selama user belum menginputkan 10 program akan tetap berjalan.

86-96 opsi yang akan ditampilkan ke user
