# Sistem Mengurutkan Stok Barang di Koperasi
## Deskripsi Singkat
Program ini adalah aplikasi sederhana berbasis teks yang berfungsi untuk mencatat dan mengelola data stok barang di sebuah koperasi. Tujuan utama dari program ini adalah membantu petugas koperasi memantau persediaan dengan cara mengurutkan daftar barang secara otomatis dari jumlah stok yang paling sedikit hingga paling banyak. Dengan begitu, petugas bisa lebih cepat mengambil keputusan terkait barang apa saja yang perlu segera dipesan ulang (restock). 

Dalam penyelesaiannya, program ini mengimplementasikan algoritma pengurutan exchange sort untuk memproses pertukaran posisi data. Sementara itu, struktur data yang diterapkan adalah array satu dimensi (implementasinya menggunakan list) yang di dalamnya menampung objek dictionary agar pasangan data antara nama barang dan jumlah stoknya dapat tersimpan secara rapi dalam satu kesatuan.

## Source Code

<img width="347" height="156" alt="Screenshot 2026-05-04 212913" src="https://github.com/user-attachments/assets/5ccfdb6c-d286-4a53-9637-521f4c1fec6d" />

Baris 1-4, membuat fungsi bernama tukar, pada baris kedua (temp = arr[i]) menyalin barang dari posisi i ke sebuah tempat bernama temp. Baris ketiga mengisi posisi i dengan barang dari posisi j. Baris keempat mengambil barang yang tadi diletakkan di temp, lalu menaruhnya di posisi j.

<img width="452" height="86" alt="Screenshot 2026-05-04 213254" src="https://github.com/user-attachments/assets/d7edfcda-2d07-4b2f-a1e8-ab965d409fb4" />

Baris 6 membuat fungsi utama untuk mengurutkan barang, tempat dimana program akan berjalan untuk menyelesaikan studi kasus ini, dengan arr (daftar barang) dan n (jumlah total barang).
Baris 7 yaitu melakukan perulangan, kenapa n - 1? karena yang akan dibandingkan tidak semua elemen maka dari itu n - 1, jika elemen sudah terurut otomatis elemen paling akhir adalah elemen terbesar jadi tidak perlu di bandingkan lagi.
Baris ke 8 yaitu melakukan perulangan kedua, disini akan mengecek sisa barang lain yang ada di sebelah kanan dari posisi i. Maka dari itu dia i + 1.

<img width="641" height="62" alt="Screenshot 2026-05-04 213416" src="https://github.com/user-attachments/assets/d5662ab1-39f4-42b1-810e-ede74fe89e87" />

Pada baris 9 dan 10 yaitu dilakukan pengecekan apakah jumlah stok di posisi kiri (i) lebih besar dari stok di posisi kanan (j). Jika iya, akan di tukar agar barang yang stoknya sisa sedikit berpindah ke sebelah kiri.

<img width="215" height="54" alt="Screenshot 2026-05-04 214343" src="https://github.com/user-attachments/assets/fe179879-6081-43c7-be0e-2382996e1152" />
Baris 12 dan 13 def(main) ibarat tempat dimana program akan mulai jalan dari sini. lalu try, program mencoba menjalankan perintah dibawahnya, disini juga antisipasi kalau nanti ada error.

<img width="887" height="34" alt="Screenshot 2026-05-04 214441" src="https://github.com/user-attachments/assets/670baee9-2293-4f58-887b-ccb63aa199eb" />
Baris 14 memunculkan teks pertanyaan di layar, lalu mengubah jawaban yang diketik menjadi angka bulat (int) dan menyimpannya di huruf n.

<img width="496" height="90" alt="Screenshot 2026-05-04 214543" src="https://github.com/user-attachments/assets/5d83ccd8-6236-4d18-8a65-4bb3cecd7bc0" />

Baris 15 dan 17 jika ternyata yang diketik bukan angka (misalnya huruf "A"), program menangkap error tersebut di sini. Dan return menampilkan pesan bahwa input salah, lalu return langsung menghentikan program agar tidak error.

<img width="472" height="64" alt="Screenshot 2026-05-04 215344" src="https://github.com/user-attachments/assets/c3796f35-d710-49d4-8bb0-4a981f921d7b" />

Baris 19 dan 20 membuat sebuah daftar kosong bernama arr untuk menyimpan semua data barang nanti. Lalu mencetak tulisan ke layar. 

<img width="333" height="42" alt="Screenshot 2026-05-04 215704" src="https://github.com/user-attachments/assets/32fd5a45-cbbd-475c-8145-1c16a1707f9e" />

Baris 21 melakukan perulangan untuk meminta data barang baru sebanyak n kali.

![Uploading Screenshot 2026-05-04 215810.png…]()
Baris 22 meminta untuk menginputkan nama barang, fungsi i + 1 untuk memulai perhitungan dari satu (Nama barang ke-1) karena pada komputer ia akan selalu memulai dari 0 maka dari itu i + 1.

Baris 23 dan 24 memulai perulangan tanpa henti khusus untuk menanyakan jumlah stok (sampai pengguna benar-benar mengetik angka). Lalu mencoba menjalankan perintah input stok.

Baris 25 meminta pengguna mengetik jumlah stok berupa angka, dan menyimpannya di variabel nilai.

Baris 26 menambagkan nama barang dan stoknya sekaligus sebagai satu pasangan ke dalam keranjang arr yang tadi kosong.

Baris 27 kalau angkanya berhasil dimasukkan, hentikan paksa perulangan while true ini dan lanjut ke barang berikutnya.

Baris 28 menangkap error jika stok diisi huruf, lalu meminta pengguna mengulang memasukkan angka.

Baris 29 mencetak teks judul ke layar.

Baris 30 membaca isi arr satu per satu.

Baris 31 menampilkan teks berupa nama barang dan jumlah stoknya ke layar.

Baris 32 mengirim arr ke bagian pengurutan agar datanya di rapikan.

Baris 33 mengulangi proses pencetakan teks seperti sebelumnya, tapi kali ini datanya sudah terurut. 

Baris 35 dan 36 memastikan bahwa program utama ini hanya akan berjalan jika file ini memang sengaja dijalankan secara langsung. Lalu menekan tombol "Start" untuk mulai mengeksekusi semua baris kode yang ada di dalam def main().
























