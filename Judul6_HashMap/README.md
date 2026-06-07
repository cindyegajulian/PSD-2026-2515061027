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

Baris 16-26 Fungsi untuk menambah data baru atau menimpa data lama, lalu menghitung lokasi indeks untuk data ini. Lalu current menunjuk ke elemen pertama di indeks tersebut. Selanjutnya looping untuk mengecek node satu per satu di dalam indeks tersebut, lalu mengecek apakah nomor peserta sudah ada sebelumnya, jika sudah ada, update nilai TKA-nya dengan yang baru. Lalu return: untuk mennghentikan fungsi setelah data di-update.

current = current.next: (Bagian dari proses looping) Pindah ke node selanjutnya jika Key belum cocok.

new_node = Node(key, value): Jika proses looping selesai dan Key tidak ditemukan, buat objek node baru.

new_node.next = self.table[index]: Sambungkan node baru tersebut ke posisi terdepan antrean pada indeks tersebut.

self.table[index] = new_node: Perbarui kepala antrean indeks agar menunjuk secara resmi ke node baru ini.
