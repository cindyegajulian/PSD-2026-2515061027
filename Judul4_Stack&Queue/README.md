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

Baris 5 & 6 Penanda posisi, front untuk depan, dan rear untuk belakang antrian. Nilai -1 maksudnya antrian masih kosong.



