# Program Pengecekan Nilai Mahasiswa yang Lulus KKM
## Deskripsi Singkat
Program ini berfungsi untuk membantu dosen atau asisten dosen untuk mengecek ada berapa mahasiswa yang berhasil lulus kuis berdasarkan KKM. Pengguna cukup memasukkan target KKM yang diinginkan, dan program akan secara otomatis menghitung jumlah mahasiswa yang mendapatkan nilai sama dengan atau lebih besar dari batas tersebut. 

Algoritma yang diterapkan adalah sequential search menggunakan struktur data list (array). Sesuai namanya, algoritma ini akan berjalan dari indeks paling awal hingga akhir untuk memeriksa data satu per satu. 

## Source Code 
<img width="512" height="250" alt="Screenshot 2026-05-09 223750" src="https://github.com/user-attachments/assets/6c7f2f61-d7f9-41b5-b778-9bcc8de1a8ea" />

Baris 1 terdapat sebuah fungsi yaitu fungsi sequential search dengan 3 parameter, data (berisi nilai mahasiswa), n (jumlah total data), dan target (batas nilai KKM yang ingin di cek).

Baris 2 ada variabel i dengan nilai 0. Berfungsi sebagai indeks karena pada python dimulai dari 0 yang akan mengarahkan program membaca data dari urutan paling pertama. 

Baris 3 ada variabel counter dengan nilai awal 0. Berfungsi untuk menghitung jumlah nilai mahasiswa yang memenuhi syarat KKM.

Baris 4 melakukan perulangan
