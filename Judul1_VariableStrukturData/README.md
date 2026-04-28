# Sistem Rekapitulasi dan Pengecekan Memori Nilai Kuis Mahasiswa
## Deskripsi Singkat
Program ini adalah aplikasi sederhana berbasis teks untuk mencatat nilai kuis mahasiswa, dan untuk membantu memahami bagaimana cara kerja memori di belakang layar. Melalui menu yang disediakan, kita bisa menginputkan nilai untuk lima mahasiswa dan melihar rekap hasil akhirnya. Fitur yang ada bukan hanya untuk menyimpan data, tapi program ini juga bisa menampilkan memory addres (alamat memori) dari array utamanya maupun dari masing-masing indeksnya. 

Program ini menggunakan struktur data array satu dimensi (implementasinya menggunakan list) untuk menampung kelima data nilai tersebut kedalam satu variabel. Program ini menggabungkan looping while agar menu utamanya bisa terus berjalan berulang-ulang, serta perulangan for untuk menelusuri indeks array satu per satu saat proses input data dan pengecekan memori. Agar program aman dan tidak error sama pengguna salah memasukkan huruf, disini diterapkan exception handling atau penanganan error menggunakan blok try except.
## Source Code
<img width="851" height="173" alt="Screenshot 2026-04-28 124013" src="https://github.com/user-attachments/assets/4c17bf36-284a-44ea-97fa-bc1fade6028b" />

Baris 1-7 adalah fungsi menu() yang isinya sekumpulan perintah print untuk menampilkan judul program dan pilihan (1-4) ke layar supaya bisa dibaca oleh pengguna.  menu atau perintah yang nantinya akan muncul pada tampilan antarmuka.

<img width="368" height="76" alt="Screenshot 2026-04-28 151619" src="https://github.com/user-attachments/assets/46461475-dbab-4483-ba29-71e228e3cca2" />

Baris ke 9-11 membuat fungsi utama (def(main)) sebagai inti program. Lalu membuat list untuk menampung nilai 5 mahasiswa. List ini langsung diisi dengan 5 angka nol. Selanjutnya membuat variabel bernama running yang nilainya adalah true, jadi selama nilainya true, program akan terus berjalan dalam looping.

<img width="248" height="50" alt="Screenshot 2026-04-28 151746" src="https://github.com/user-attachments/assets/744bb5f6-9d52-47e3-b742-1b71b902dab7" />

Baris ke 12 dan 13 memulai perulangan utama, selama nilainya masih true akan terus kembali ke menu awal dan memanggil fungsi menu yang sudah dibuat pada baris ke 1 untuk ditampilkan ke layar.


<img width="522" height="120" alt="Screenshot 2026-04-28 151914" src="https://github.com/user-attachments/assets/c8bfe88e-0948-49f5-8da4-79fc3cd2b5a6" />

Baris ke 14-18 untuk mencoba menerima input dari pengguna lewat variabel choice. Lalu pakai blok try except untuk antisipasi jika pengguna salah memberi masukkan (input). Kalau salah, program akan memberi peringatan dan perintah continue yang membuat program kembali ke menu tanpa mengalami error.


<img width="900" height="55" alt="Screenshot 2026-04-28 152024" src="https://github.com/user-attachments/assets/4077b77b-c5ee-41ab-8714-d13697ab8b35" />

Baris 19 dan 20 jika pengguna pilih 1, program bakal nampilin alamat di memori tempat list disimpan, menggunakan bantuan fungsi id().

<img width="1104" height="79" alt="Screenshot 2026-04-28 152103" src="https://github.com/user-attachments/assets/6443f958-a996-4afa-a45f-5382d2ca1ff3" />

Baris 21-23 jika pengguna memilih 2, program akan ngejalanin perulangan for sebanyak 5 kali untuk melakukan pengecekan dan nampilin alamat memori spesifik dari tiap slot (indeks) mahasiswa yang ada di dalam list tersebut.

<img width="640" height="49" alt="Screenshot 2026-04-28 152154" src="https://github.com/user-attachments/assets/a1d005ef-d69c-45fc-9f29-3ce97f87440c" />

Baris 24 dan 25 jika pengguna memilih 3, program akan memberi intruksi awal untuk mulai proses input nilai.

<img width="988" height="123" alt="Screenshot 2026-04-28 152244" src="https://github.com/user-attachments/assets/5b057d02-d23c-4262-91f9-3348e209c12e" />

Baris 26-30 program melakukan looping untuk meminta nilai kelima mahasiswa secara berurutan. Di dalamnya terdapat looping while true agar ketika nilai berhasil dimasukkan, perulangan di break dan lanjut ke mahasiswa berikutnya.

<img width="788" height="50" alt="Screenshot 2026-04-28 152347" src="https://github.com/user-attachments/assets/80f0d1f4-45dc-47fc-a1ef-580542dc90f9" />

Baris 31 dan 32 lanjut dari input tadi. Kalau ternyata pengguna salah masukin huruf (bukan angka), bagian ini akan menangkap error dan memberikan peringatan. Karena ada while true tadi, program akan minta ulang nilai di mahasiswa yang salah, tanpa harus ulang dari mahasiswa pertama.

<img width="740" height="28" alt="Screenshot 2026-04-28 152424" src="https://github.com/user-attachments/assets/6f529ece-84a1-4036-9da2-76b70400a990" />

Baris ke 33, setelah looping input 5 mahasiswa selesai, baris ini akan menampilkan bentuk list akhir yang sekarang sudah berisi angka nilai-nilai tersebut

<img width="631" height="76" alt="Screenshot 2026-04-28 152651" src="https://github.com/user-attachments/assets/8d69eee2-8660-423e-869d-5c4a3c4a7e59" />

Baris 34-36 jika user memilih angka 4, variabel penanda running berubah jadi false. Ini otomatis akan menghentikan looping utama while, lalu menampilkan pesan penutup sebelum program benar-benar berhenti.

<img width="473" height="51" alt="Screenshot 2026-04-28 152746" src="https://github.com/user-attachments/assets/fdd2beb8-65e9-4fce-ba2d-bb5596d96ccc" />

Baris 37 dan 38 berfungsi untuk memberikan peringatan jika pengguna memasukkan angka selain yang tertera pada pilihan (1-4).

<img width="325" height="47" alt="image" src="https://github.com/user-attachments/assets/07628094-b321-4a84-9cee-711c225202a0" />

Baris 40 dan 41 untuk memastikan fungsi main() langsung dieksekusi dari awal saat program ini dijalankan.

## Output

<img width="634" height="187" alt="Screenshot 2026-04-28 182934" src="https://github.com/user-attachments/assets/34cb1d11-fc58-40e0-be2c-38637d9ce9ec" />

Saat program pertama kali dieksekusi, menu utama langsung muncul dengan baik, lalu ketika opsi 1 dipilih, program berhasil mencetak alamat memori utama dari list penyimpan nilai.

<img width="627" height="277" alt="Screenshot 2026-04-28 182954" src="https://github.com/user-attachments/assets/f1fd564d-2463-457d-ab22-ef1d44b2a4d5" />

Ketika opsi 2 dipilih, program menampilkan 5 baris alamat memori yang berbeda untuk masing-masing slot (indeks) nilai mahasiswa.

<img width="625" height="348" alt="Screenshot 2026-04-28 184329" src="https://github.com/user-attachments/assets/34368109-201b-444c-8b1b-f2b533f5d003" />
333

<img width="636" height="195" alt="Screenshot 2026-04-28 183136" src="https://github.com/user-attachments/assets/9e88620d-ff26-424d-be81-6c5a238e75b7" />

aaaa

<img width="628" height="183" alt="Screenshot 2026-04-28 183200" src="https://github.com/user-attachments/assets/ce4b4fdb-b347-4d8f-a6c2-331d40dd456d" />

4















