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

<img width="891" height="87" alt="Screenshot 2026-05-09 232154" src="https://github.com/user-attachments/assets/f1d5b152-1ed6-4e27-8b04-53b0ea1b81e5" />

Baris 11 menyimpan daftar nilai ke list data.

Baris 12 menghitung otomatis berapa banyak elemen yang ada di list data.

Baris 13 menampilkan isi dari data ke layar.

<img width="1037" height="182" alt="Screenshot 2026-05-09 232616" src="https://github.com/user-attachments/assets/08057515-d786-47a2-baab-eabeac2fcc7f" />

Baris 14, perulangan yang fungsinya untuk meminta pengguna agar memberikan inpur berupa angka.

Baris 15 program mencoba menjalankan perintah yang akan memungkinkan mengalami error (seperti ketika diminta input angka tetapi yang diinputkan huruf).

Baris 16 menampilkan teks untuk meminta pengguna mengiputkan batas nilai KKM dan menyimpannya ke variabel target.

Baris 17 untuk keluar dari perulangan ketika pengguna menginputkan sesuai yang diminta yaitu angka.

Baris 18 menangkap error jika pengguna memasukkan huruf atau simbol selain angka.

Baris 19 menampilkan pesan peringatan untuk pengguna agar memberikan input yang benar. Lalu akan kembali ke perulangan untuk meminta input ulang.

<img width="639" height="33" alt="Screenshot 2026-05-09 233626" src="https://github.com/user-attachments/assets/62bd9ca3-e776-4d7f-a3d3-c43c2e1325a0" />
Baris 21 memanggil fungsi sequential search lalu jumlah mahasiswa yang berhasil dihitung disimpan ke variabel counter.

<img width="1315" height="117" alt="Screenshot 2026-05-10 002604" src="https://github.com/user-attachments/assets/4275662d-4331-4c67-b4a9-add955c8e1d4" />

Baris 23 memeriksa apakah counter lebih besar dari 0 yang artinya ada mahasiswa yang lulus KKM.

Baris 24 jika ada yang lulus, program memberitahukan ke pengguna total mahasiswa yang lulus atau memenuhi batas KKM. 

Baris 25 jika kondisi tidak terpenuhi atau counter tepat 0. 

Baris 26 menampilkan pemberitahuan ke pengguna bahwa tidak  ada satupun mahasiswa yang lulus KKM. 

<img width="384" height="68" alt="Screenshot 2026-05-09 235448" src="https://github.com/user-attachments/assets/2163f11b-d708-4285-be0a-902bfa7d13be" />

Baris 28 memastikan bahwa program utama ini hanya akan berjalan jika sengaja dijalankan secara langsung. 

Baris 29 memanggil fungsi main untuk mengeksekusi seluruh program, dari awal sampai akhir.

## Output

<img width="919" height="85" alt="Screenshot 2026-05-10 002842" src="https://github.com/user-attachments/assets/50525675-69c5-4902-9de1-d4f218d73ced" />

Ketika program dijalankan mula-mula akan menampilkan data nilai untuk di neritahukan ke pengguna, lalu meminta pengguna untuk menginputkan batas nya atau KKM nya. Baru setelah itu program melakukan pencarian ada berapa nilai yang lebih dan sama dengan KKM.

<img width="918" height="77" alt="Screenshot 2026-05-10 001247" src="https://github.com/user-attachments/assets/50688788-9483-4344-80e3-8d7f7e9bbe7a" />

Awalnya sama, menampilkan data lalu meminta pengguna menginputkan KKM nya, lalu karena tidak ada nilai diatas atau sama dengan 90 maka program akan memberitahu bahwa tidak ada mahasiswa yang mencapai KKM.

## Link Youtube









