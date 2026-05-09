# Program Pengecekan Nilai Mahasiswa yang Lulus KKM
## Deskripsi Singkat
Program ini berfungsi untuk membantu dosen atau asisten dosen untuk mengecek ada berapa mahasiswa yang berhasil lulus kuis berdasarkan KKM. Pengguna cukup memasukkan target KKM yang diinginkan, dan program akan secara otomatis menghitung jumlah mahasiswa yang mendapatkan nilai sama dengan atau lebih besar dari batas tersebut. 

Algoritma yang diterapkan adalah sequential search menggunakan struktur data list (array). Sesuai namanya, algoritma ini akan berjalan dari indeks paling awal hingga akhir untuk memeriksa data satu per satu. 

## Source Code 
<img width="512" height="250" alt="Screenshot 2026-05-09 223750" src="https://github.com/user-attachments/assets/6c7f2f61-d7f9-41b5-b778-9bcc8de1a8ea" />

Baris 1 terdapat sebuah fungsi yaitu fungsi sequential search dengan 3 parameter, data (berisi nilai mahasiswa), n (jumlah total data), dan target (batas nilai KKM yang ingin di cek).

Baris 2 ada variabel i dengan nilai 0. Berfungsi sebagai indeks karena pada python dimulai dari 0 yang akan mengarahkan program membaca data dari urutan paling pertama. 

Baris 3 ada variabel counter dengan nilai awal 0. Berfungsi untuk menghitung jumlah nilai mahasiswa yang memenuhi syarat KKM.

Baris 4 melakukan perulangan. Program akan terus melakukan perulangan selama nilai indeks masih kurang dari total panjang data. Ini memastikan semua nilai dari awal hingga akhir diperiksa tanpa ada yang terlewat.

Baris 5 program akan memeriksa apakah nilai mahasiswa pada urutan ke-i lebih besar atau sama dengan nilai target (KKM).

Baris 6 jika pengecekan pada baris 5 bernilai benar maka angka pada variabel counter akan ditambah 1.

Baris 7 nilai indeks i akan terus ditambah 1 sampai akhir putaran agar program terus bergeser maju untuk memeriksa nilai mahasiswa di urutan selanjutnya.

Baris 8 akan mengembalikan hasil akhir dari perhitungan yang tersimpan di dalam variabel counter ke tempat fungsi ini dipanggil nantinya.

<img width="202" height="36" alt="Screenshot 2026-05-09 231437" src="https://github.com/user-attachments/assets/0ca91b81-369d-449d-96df-b6bb17583d71" />

Baris 10 membuat fungsi utama bernama main(). Disini alur program berjalan dari awal sampai menampilkan hasil akhir.







