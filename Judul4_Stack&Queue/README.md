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

<img width="512" height="91" alt="image" src="https://github.com/user-attachments/assets/91738223-428b-483f-8c45-79f10b5d1eda" />
 Baris 47-49






