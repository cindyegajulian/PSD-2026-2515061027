# Sistem Pengelolaan Skor TKA
## Deskripsi  Singkat
Program ini membantu panitia ujian mengelola skor TKA secara efisien, meliputi proses penambahan (Insert), pencarian (Search), penghapusan (Remove), dan rekapitulasi data.

Program ini menerapkan struktur data Hash Table dengan teknik Separate Chaining. Data peserta didistribusikan ke dalam indeks tabel menggunakan operasi modulus. Jika ada beberapa peserta yang menempati indeks yang sama (collision), data mereka akan dirangkai menjadi antrean Linked List. Metode ini menjamin proses pengelolaan data tetap sangat cepat dan memastikan tidak ada nilai peserta yang hilang tertimpa.

## Source Code 
<img width="405" height="122" alt="image" src="https://github.com/user-attachments/assets/a031c6ee-a57c-4ea9-9583-38ab226a86f2" />

Baris 1-5 inisialisasi class untuk menyimpan data, lalu fungsi untuk menyimpan tiga parameter yaitu key, value, dan next. Key untuk menyimpan nomor peserta, value untuk menyimpan skor TKA, dan next untuk menunjuk ke node selanjutnya.

<img width="626" height="171" alt="image" src="https://github.com/user-attachments/assets/8b229838-78ab-4b84-9eb8-cf180d7a7011" />

Baris 8-14 inisaialisasi class utama, lalu fungsi dengan kapasitas awal 10, self.size = size: digunakan untuk menyimpan batas ukuran tabel, yaitu 10, lalu membuat tvabel kosong berisi none sebanyak kapasitas size.

Selanjutnya fungsi hash, disini untuk menghitung key akan masuk ke indeks ke berapa, lalu rumus modulus untuk mengubah key menjadi indeks yang valid dan menjamin hasil tidak negatif.

<img width="471" height="266" alt="image" src="https://github.com/user-attachments/assets/7fb20c07-693d-4b4a-b2ae-ce0ade95fe1a" />

Baris 16-26 Fungsi untuk menambah data baru atau menimpa data lama, lalu menghitung lokasi indeks untuk data ini. Lalu current menunjuk ke elemen pertama di indeks tersebut. Selanjutnya looping untuk mengecek node satu per satu di dalam indeks tersebut, lalu mengecek apakah nomor peserta sudah ada sebelumnya, jika sudah ada, update nilai TKA-nya dengan yang baru. Lalu return: untuk mennghentikan fungsi setelah data di-update. Lalu current.next untuk pindah ke node selanjutnya jika key belum cocok. Selanjutnya jika proses looping selesai dan key tidak ditemukan, buat objek node baru. Nah lanjut lagi untuk menyambungkan node baru yang sudah dibuat ke posisi terdepan antrian pada indeks tersebut. Terakhir mengganti indeks paling awal dengan node baru.

<img width="446" height="195" alt="image" src="https://github.com/user-attachments/assets/6d20cafe-3da4-4dfd-b3ba-098d60562feb" />

Baris 28-35 membuat fungsi untuk mencari data skor berdasarkan nomor peserta. Selanjutnya mencari tau di indeks mana data ini disimpan. Lalu current disini menunjuk ke elemen awal di linkedlist tersebut. Lalu mengecek apakah current tidak kosong. Jika current.key == key artinya nomor peserta yanag dicari sudah ditemukan. Lalu mengembalikan node tersebut sebagai hasil pencarian. Lalu current = current.next: jika belum cocok, lanjut ke node berikutnya. Terakhir jika node sudah habis dieksplor dan tidak ketemu, kembalikan none (Kosong).

<img width="568" height="337" alt="image" src="https://github.com/user-attachments/assets/547d3522-83eb-4a8f-b590-d00a5c195aa8" />

Baris 37-50 fungsi untuk menghapus peserta dari sistem. Selanjutnya mencari tau di indeks mana data ini disimpan. Lalu current menunjuk node pertama. Lalu variabel prev untuk mengingat node "sebelumnya" agar bisa menyambung rantai saat ada yang dicopot. Lalu mengecek apakah current tidak kosong. Nah current.key == key: kondisi jika node yang akan dihapus akhirnya ketemu. Lalu jika kebetulan node tersebut berada tepat di urutan paling pertama, hapus node pertama dengan cara langsung menunjuk node kedua sebagai ujung antrian. else: Jika node yang mau dihapus berada di tengah atau di akhir lalu akan menyambungkan node sebelumnya langsung ke node selanjutnya (melewati node yang dihapus). return True: memberikan respons True bahwa penghapusan berhasil. Selanjutnya selalu menyimpan node saat ini ke variabel prev sebelum maju. current = current.next: maju menelusuri node selanjutnya. Terakhir memberikan respons False jika seluruhnya sudah dicek tapi data tidak ada.

<img width="735" height="223" alt="image" src="https://github.com/user-attachments/assets/ce3c2854-3237-4f73-b142-5bcfa35a43c2" />

Baris 52-60 fungsi untuk memvisualisasi sistem. Lalu mencetak teks judul, selanjutnya melakukan iterasi berulang pada indeks ke-0 sampai ke-9. Lalu menampilkan angka untuk nomor urut, selanjutnya mengambil elemen pertama dari indeks saat ini. Seperti sebelumnya mengecek apakah current tidak kosong. Lalu mencetak nomor peserta dan skor TKA. Selanjutnya geser ke node berikutnya untuk dicetak. Terakhir mencetak batas akhir yang menandakan node selanjutnya sudah kosong.

<img width="1020" height="604" alt="image" src="https://github.com/user-attachments/assets/0a75048f-41f3-4198-9c43-d629d8781a77" />

Baris 63-87 fungsi dimana kode utama akan dieksekusi. Selanjutnya menginisialisasi sistem hashtable dan menyimpannya di variabel hashmap.Lalu melakukan proses input nomor peserta dan skornya ke sistem berulang kali. Lalu mencetak teks pemisah dan menampilkan visualisasi keseluruhan tabel. Nah selanjutnya mendefinisikan variabel nomor peserta yang ingin dicoba dicari skornya. Lalu memanggil fungsi pencarian untuk mencari keberadaan nomor peserta 11. Selanjutnya jika ketemu (tidak None), cetak nilainya. Jika tidak, cetak teks "tidak ditemukan". Lalu memerintahkan sistem menghapus data nomor peserta 11. Dan terakhir mencetak ulang tabel sistem untuk membuktikan bahwa data tersebut telah sukses dihapus tanpa merusak susunan data lain.

Terakhir memastikan agar fungsi main() dieksekusi hanya ketika file dijalankan langsung.

## Output
<img width="510" height="670" alt="Screenshot 2026-06-07 131308" src="https://github.com/user-attachments/assets/4ae66952-7dfc-4efc-88f4-3ecfe8c8a1c5" />

Output dari semua logika yang ada. Awalnya, terlihat penumpukan data di laci nomor 1, sehingga data peserta 21, 11, dan 1 terpaksa mengantre saling bersambung membentuk list. Kemudian, program membuktikan bisa mencari dan memunculkan skor peserta nomor 11 dari dalam antrian tersebut. Terakhir, saat data peserta 11 dihapus, sistem menunjukkan bahwa datanya berhasil dicabut dari tengah antrian dengan aman, sehingga sisa datanya (peserta 21 dan 1) langsung menyambung kembali tanpa membuat listnya terputus.

## Link Youtube
https://youtu.be/a4X88CYS8ds
