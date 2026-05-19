# Sistem Antrian Digital Warung Mak Enah
## Deskripsi Singkat
Program dibuat untuk mengimplementasikan antrian  di  sebuah warung bernama Warung Mak Enah. Tamu akan mendapatkan meja dan giliran, dengan cukup mendaftar ke bagian kasir yang nantinya akan dicatat oleh kasir. Lalu akan dipanggil sesuai urutan kedatangan. Program ini memiliki 4 fitur utama yaitu mendaftarkan tamu baru (enqueue), memanggil tamu paling depan saat meja tersedia (dequeue), melihat siapa tamu berikutnya tanpa mengeluarkan dari antrian (peek), dan menampilkan seluruh daftar antrian yang sedang menunggu (display).

Algoritma struktur data yang digunakan adalah queue (antrian). Prinsip  kerjanya sama seperti antrian pada umumnya yaitu, siapa yang datang duluan, akan dilayani duluan. Konsep ini disebut FIFO (First In First Out).

## Source Code 
<img width="309" height="33" alt="Screenshot 2026-05-17 091237" src="https://github.com/user-attachments/assets/6eedeac6-f70a-43f2-ba27-39d7fa0fafcb" />

Baris 1 kita buat terlebih dahulu sebuah class dengan nama AntrianWarung yang nantinya semua yang berhubungan dengan Antrian ada di sini.

<img width="486" height="34" alt="Screenshot 2026-05-17 091449" src="https://github.com/user-attachments/assets/9f321217-f2d5-4048-8521-5ed56fe5ffe3" />

Baris 2 fungsi utama dari logika antrian. Kapastias=10 berperan sebagai maxsize nya atau seperti slotnya kosongnya, jadi ada 10 slot.

<img width="403" height="33" alt="Screenshot 2026-05-17 091810" src="https://github.com/user-attachments/assets/8b4efe32-fc16-433f-b207-7695136da580" />

Baris 3 menyimpan nilai kapasitas ke variabel MAXN, yang nantinya akan jadi batas maksimal antrian.

<img width="478" height="31" alt="Screenshot 2026-05-17 092441" src="https://github.com/user-attachments/assets/acbc3d6a-d223-4b77-bba9-a9b1c88f90a1" />

Baris 4 membuat array sepanjang MAXN yang isinya kosong semua, atau None. Ini akan menjadi tempat duduk para tamju, makanya di awal kosong semua.

<img width="381" height="61" alt="Screenshot 2026-05-17 092933" src="https://github.com/user-attachments/assets/0d5d8f9a-f37d-437b-bf93-8f1218a806ef" />

Baris 5 & 6 Penanda posisi, front untuk depan, dan rear untuk belakang antrian. Nilai -1 maksudnya antrian masih kosong. Karena indeks array dimulai dari 0, maka dari itu untuk front dan rearnya adalah -1 karena jika 0 maka antrian sudah terisi diposisi pertama.

<img width="346" height="30" alt="Screenshot 2026-05-17 094824" src="https://github.com/user-attachments/assets/b61d2732-5e49-4aea-ade8-71b2c4b3b9ee" />

Baris 7 untuk menghitung nomor antrian secara otomatis. Jadi akan naik setiap ada tamu baru (1, 2, 3....).

<img width="513" height="67" alt="Screenshot 2026-05-17 095058" src="https://github.com/user-attachments/assets/0bfadaff-426e-480c-8f9a-9f98b37a5f0c" />

Baris 9 & 10 fungsi untuk memeriksa antrian kosong atau tidak. Ketika front_idx masih -1, berarti belum ada tamu, lalu return true.

<img width="819" height="63" alt="Screenshot 2026-05-17 095359" src="https://github.com/user-attachments/assets/787c66b0-faf3-48d3-afdb-89589a98324f" />

Baris 12 & 13 untuk memeriksa  antrian apakah penuh atau tidak. Pakai % MAXN karena antriannya circular (melingkar). Ketika slot tepat setelah rear sudah menyentuh front, artinya penuh.

<img width="496" height="38" alt="Screenshot 2026-05-17 095504" src="https://github.com/user-attachments/assets/678e5ede-8c3f-4863-b913-3ca4af51b313" />

Baris 15 membuat fungsi untuk menambahkan tamu baru ke antrian, menerima parameter nama dan jumlah.

<img width="868" height="92" alt="Screenshot 2026-05-17 100107" src="https://github.com/user-attachments/assets/d2dde8be-ad66-4922-9049-6067ecb88ef8" />

Baris 16-18 ketika array penuh dengan kapasitas 10 yang sudah dijelaskan diawal, program akan memberi tau dan akan berhenti (return).

<img width="375" height="32" alt="Screenshot 2026-05-17 100904" src="https://github.com/user-attachments/assets/f5d9d3bd-2aa0-47ef-a194-0e7b6a3a2626" />

Baris 19 untuk menaikkan counter yang digunakan untuk menambah nomor antrian baru. 

<img width="1006" height="33" alt="Screenshot 2026-05-17 101307" src="https://github.com/user-attachments/assets/8bd1e542-045d-4f1f-a740-3fa76f2e1f2c" />

Baris 20 membuat data tamu dengan dictionary. Berisi nomor, (formatnya A01, A02 dan seterusnya (A untuk antrian, 02d untuk minimal angka yaitu 2 digit, misal 1 jadi 01)), nama, dan jumlah orang.

<img width="609" height="61" alt="Screenshot 2026-05-17 101541" src="https://github.com/user-attachments/assets/4f62cf07-20f3-46d8-a913-7e0df9faa130" />

Baris 21 & 22 jika antrian kosong tamu pertama masuk di slot 0.

<img width="758" height="60" alt="Screenshot 2026-05-17 103625" src="https://github.com/user-attachments/assets/e784407a-1c3f-41e2-9ba9-508936354f20" />

Baris 23 & 24 jika sebelumnya sudah ada tamu, geser posisi belakang satu slot. Menggunakan % MAXN agar ketika sudah diujung array, ia akan balik lagi ke awal (circular).

<img width="496" height="34" alt="Screenshot 2026-05-17 103717" src="https://github.com/user-attachments/assets/c0468380-7427-4ee5-bccc-b0c0512b9e84" />

Baris 25 menyimpan data tamu ke slot belakang yang barusan digeser. 

<img width="837" height="40" alt="Screenshot 2026-05-17 103732" src="https://github.com/user-attachments/assets/91aa2e50-063c-4b23-a9f1-2d96b13c5225" />

Baris 26 memberikan pesan bahwa tamu sudah berhasil masuk ke antrian.

<img width="335" height="35" alt="Screenshot 2026-05-17 104609" src="https://github.com/user-attachments/assets/f9b91b04-da18-4101-8dd6-2ec0cde8e0f7" />

Baris 28 fungsi untuk memanggil atau mengeluarkan tamu paling depan (yang duluan dateng, duluan dipanggil).

<img width="859" height="90" alt="Screenshot 2026-05-17 104747" src="https://github.com/user-attachments/assets/d4c807d2-ebec-458c-9c3d-186dcb807f63" />

Baris 29-31 jika antrian kosong, program akan berhenti (return) dan menampilkan pesan "Antrian kosong! Tidak ada tamu yang menunggu".

<img width="475" height="30" alt="Screenshot 2026-05-17 105617" src="https://github.com/user-attachments/assets/1c035ebd-f03d-4844-9351-c76c42e30160" />

Baris 32 mengambil data tamu diposisi paling depan .

<img width="976" height="38" alt="Screenshot 2026-05-17 105657" src="https://github.com/user-attachments/assets/c6b31baf-4832-4664-9aa4-99b07b58d751" />

Baris 33 memberitaukan siapa tamu yang dipanggil. 

<img width="625" height="60" alt="Screenshot 2026-05-17 105724" src="https://github.com/user-attachments/assets/ff92856f-6891-415c-a659-3a2d86501356" />

Baris 34 & 35 jika tamu yang dipanggil adalah satu-satunya tamu, setelah keluar  antrian jadi kosong, maka akan mereset keduanya ke -1.

<img width="795" height="60" alt="Screenshot 2026-05-17 112656" src="https://github.com/user-attachments/assets/28fcb3aa-4e04-4b3b-8901-848996658d8e" />

Baris 36 & 37 jika masih ada tamu lain, geser (front_idx) satu slot ke depan secara circular.

<img width="301" height="33" alt="Screenshot 2026-05-17 113208" src="https://github.com/user-attachments/assets/603bc6f1-9818-4887-9f23-38ee295b19f3" />

Baris 39 fungsi untuk melihat tamu paling depan tanpa memanggilnya atau mengeluarkannya.

<img width="509" height="93" alt="Screenshot 2026-05-17 113246" src="https://github.com/user-attachments/assets/ff4fd1a8-faff-4446-8575-86fa8313cfc1" />

Baris 40-42 jika antrian kosong, program akan menampilan pesan lalu return. 

<img width="476" height="37" alt="Screenshot 2026-05-17 113324" src="https://github.com/user-attachments/assets/fb516983-cfb7-4af6-8326-73731dba2eac" />

Baris 43 mengambil data tamu di posisi paling depan.

<img width="977" height="37" alt="Screenshot 2026-05-17 113350" src="https://github.com/user-attachments/assets/a54ccfb7-3273-49ef-947e-ec2fea6b3cd2" />

Baris 44 menampilkan informasi tamu terdepan atau tamu berikutnya dengan nomor antrian, nama,  dan jumlah orang.

<img width="339" height="29" alt="image" src="https://github.com/user-attachments/assets/adc488a1-5382-4c6c-bf13-d8ce4b603331" />

Baris 46  fungsi untuk menampilkan seluruh isi antrian.

<img width="505" height="120" alt="image" src="https://github.com/user-attachments/assets/3b8b3306-9798-44e3-ba57-d87764f9c5ed" />

Baris 47-50 jika kosong program akan berhenti. Lalu akan mencetak semacam judul 'Isi antrian: '.

<img width="481" height="36" alt="image" src="https://github.com/user-attachments/assets/fe4b9aed-d63a-4922-9597-9f6a53f64ad5" />

Baris 51 i digunakan untuk menunjukkan posisi di array mulai dari depan, lalu pos untuk nomor urut tampilan (1, 2, 3...).

<img width="1003" height="147" alt="image" src="https://github.com/user-attachments/assets/02402723-c0d5-45b0-9d8f-b0f1dbbab33a" />

Baris 52-56 perulangan atau loop, lalu mengambil data tamu diposisi i, setelahnya menampilkan nomor antrian, nama, dan jumlah orang. Kalau i udah sampai posisi belakang, artinya semua tamu sudah ditampilkan, lalu break untuk keluar loop.

<img width="486" height="59" alt="image" src="https://github.com/user-attachments/assets/ed96dbea-d0e0-4575-bde5-3942a43859a4" />

Baris 57 & 58 geser i ke slot berikutnya secara circular, lalu naikkan nomor urut.  

<img width="552" height="85" alt="image" src="https://github.com/user-attachments/assets/8fe92887-65ef-48f8-a601-3d22fdad5d9f" />

Baris 60-62 membuat fungsi main, logika berjalannya program, lalu variabel antrian dengan kapasitas 10. Lalu inisialisasi pilih = 0 agar loop bisa dimulai. 

<img width="321" height="31" alt="image" src="https://github.com/user-attachments/assets/47582f41-2df6-4273-8c4a-ad9d05bf4594" />

Baris 63 akan terus melakukan looping selama user belum pilih 5 (keluar).

<img width="821" height="264" alt="image" src="https://github.com/user-attachments/assets/b465fdac-ece9-468c-bec8-1ec0c211423a" />

Baris 64-72 menampilkan pilihan yang ada ke layar.

<img width="764" height="142" alt="image" src="https://github.com/user-attachments/assets/051bd955-0ec8-4a9f-b1c1-88423d9d42c9" />

Baris 73-77 mencoba meminta input dari user. Ketika user menginputkan bukan angka, maka akan error lalu menampilkan pesan error dan akan lanjut ke iterasi berikutnya.

<img width="626" height="60" alt="image" src="https://github.com/user-attachments/assets/42fc180a-b3b9-4a55-87d3-047c302c280b" />

Baris 79 & 80 jika pilih 1, program akan meminta input nama tamu, lalu .strip buat bersihin spasi di awal atau akhir jika ada. 

<img width="663" height="88" alt="image" src="https://github.com/user-attachments/assets/9cbdf48c-e8fe-44ee-b6c7-569b258dddfc" />

Baris 81 & 83 ketika user menekan enter tanpa menginputkan nama maka program akan menampilkan peringatan bahwa nama tidak boleh kosong.

<img width="725" height="234" alt="image" src="https://github.com/user-attachments/assets/0f2cd62d-26e6-4c1e-b0ea-562cd0b638eb" />

Baris 84-91 meminta input jumlah orang, inputnya harus angka dan lebih besar dari 0. Nah ketika input sudah sesuai maka akan lanjut. 

<img width="277" height="16" alt="image" src="https://github.com/user-attachments/assets/e54f73ff-4f3c-40fd-a9dc-7ba2e32bb5b8" />

Baris 92 akan memanggil enqueue untuk mendaftarkan tamu.

<img width="475" height="134" alt="image" src="https://github.com/user-attachments/assets/1cb65e6c-4795-4bf3-9a81-9cc7dd78dda4" />

Baris 93-101 pilihan 2-4 akan mamnggil fungsi yang dimau, nah untuk pilihan 5 untuk keluar dari program. Ketika user menginputkan selain itu, program akan menampilkan 'pilihan tidak valid'.

<img width="203" height="34" alt="image" src="https://github.com/user-attachments/assets/632864bb-24bb-4a6b-92dc-7e2f1cb25cc5" />

Baris 104 & 105 untuk memastikan fungsi main hanya akan dijalankan ketika file ini dijalankan langsung, bukan saat di import dari file lain.

## 0utput
<img width="283" height="162" alt="image" src="https://github.com/user-attachments/assets/90586ef9-0b95-4b0d-aea6-5cf5ef1513c6" />

Output ketika user menginputkan bukan angka 1-5 dimana program akan menampilkan bahwa output tidak valid dan akan meminta input ulang.

<img width="266" height="148" alt="image" src="https://github.com/user-attachments/assets/ea290db9-e8a6-4776-be2d-eb88c6aa7df5" />

Ketika user menginputkan satu, maka program akan meminta input kembali, yaitu nama orang sebagai tamunya.

<img width="265" height="167" alt="image" src="https://github.com/user-attachments/assets/0d8fc612-f5de-410a-810a-68cf4264945f" />

Selanjutnya, ketika nama tamu sudah berhasil diinputkan, maka program akan meminta input untuk jumlah orangnya.

<img width="260" height="317" alt="image" src="https://github.com/user-attachments/assets/c24c08bf-d5bf-46ea-8e86-05e59b5223db" />

Nah ketika nama dan jumlah orang sudah berhasil diinput, program akan memberitahu ke user bahwa data berhasil disimpan. Selanjutnya akan meminta input kembali sampai user memilih 5 untuk keluar dan program baru akan berhenti.

<img width="247" height="221" alt="image" src="https://github.com/user-attachments/assets/f45da48a-12a5-40a6-a75f-ccd83eeba056" />

Nah ini untuk output ketika user memilih 4 dan sebelumnya user sudah menginputkan beberapa nama tamu.

<img width="262" height="158" alt="image" src="https://github.com/user-attachments/assets/1cd0a398-c911-4a24-8969-c438b2c33e69" />

Selanjutnya ketika user akan memanggil tamu, ini akan terurut sesuai dengan nomor urut tamu tersebut.

<img width="262" height="158" alt="image" src="https://github.com/user-attachments/assets/274ff1c1-6aec-4a05-8e37-513037a485e9" />

Ini untuk output ketika user memilih 3 untuk menampilkan tamu selanjutnya, yaitu pada nomor urut 2.

<img width="262" height="158" alt="image" src="https://github.com/user-attachments/assets/07cf7ed1-0a5b-4ed8-bb95-2841a1387d2f" />




## Link Youtube







