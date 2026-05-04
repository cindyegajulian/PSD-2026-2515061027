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

<img width="706" height="31" alt="Screenshot 2026-05-04 215810" src="https://github.com/user-attachments/assets/107fd98b-3ec6-4196-8e53-96890c3a2874" />

Baris 22 meminta untuk menginputkan nama barang, fungsi i + 1 untuk memulai perhitungan dari satu (Nama barang ke-1) karena pada komputer ia akan selalu memulai dari 0 maka dari itu i + 1.

<img width="307" height="67" alt="Screenshot 2026-05-04 220350" src="https://github.com/user-attachments/assets/d11ef0b7-d92f-48b5-adf1-40940245769c" />
Baris 23 dan 24 memulai perulangan tanpa henti khusus untuk menanyakan jumlah stok (sampai pengguna benar-benar mengetik angka). Lalu mencoba menjalankan perintah input stok.

<img width="846" height="35" alt="Screenshot 2026-05-04 220436" src="https://github.com/user-attachments/assets/b2c42d3d-f67d-4334-8406-76dd1365cf3d" />
Baris 25 meminta pengguna mengetik jumlah stok berupa angka, dan menyimpannya di variabel nilai.

<img width="821" height="33" alt="Screenshot 2026-05-04 220525" src="https://github.com/user-attachments/assets/49115236-0854-44b2-8fe0-b3d0c2f4f5c0" />
Baris 26 menambahkan nama barang dan stoknya sekaligus sebagai satu pasangan ke dalam keranjang arr yang tadi kosong.

<img width="338" height="28" alt="Screenshot 2026-05-04 220745" src="https://github.com/user-attachments/assets/5caedddc-4e2d-4938-8306-0197ea1905b5" />
Baris 27 kalau angkanya berhasil dimasukkan, hentikan paksa perulangan while true ini dan lanjut ke barang berikutnya.

<img width="849" height="61" alt="Screenshot 2026-05-04 221054" src="https://github.com/user-attachments/assets/c7c68e1b-38e3-48bd-b581-bae6613a9997" />
Baris 28 dan 29 menangkap error jika stok diisi huruf, lalu meminta pengguna mengulang memasukkan angka.



<img width="752" height="94" alt="Screenshot 2026-05-04 221913" src="https://github.com/user-attachments/assets/05cb676a-9b2d-40dc-8def-c87e3dd90520" />
Baris 30-32 mencetak teks judul ke layar, membaca isi arr satu per satu dan menampilkan teks berupa nama barang dan jumlah stoknya ke layar.

<img width="774" height="149" alt="Screenshot 2026-05-04 223316" src="https://github.com/user-attachments/assets/00147b6d-f798-4d16-9d0a-5f33e5e6acd1" />

Baris 35-38engirim arr ke bagian pengurutan agar datanya di rapikan. mengulangi proses pencetakan teks seperti sebelumnya, tapi kali ini datanya sudah terurut. 


<img width="401" height="62" alt="Screenshot 2026-05-04 221611" src="https://github.com/user-attachments/assets/576b6a41-3451-4d7d-bbe7-61e2c91b2805" />
Baris 41 dan 42 memastikan bahwa program utama ini hanya akan berjalan jika file ini memang sengaja dijalankan secara langsung. Lalu menekan tombol "Start" untuk mulai mengeksekusi semua baris kode yang ada di dalam def main().

## Output
<img width="510" height="363" alt="Screenshot 2026-05-04 213640" src="https://github.com/user-attachments/assets/e26719b2-e838-45b2-8743-84ef7d4f9446" />
Output data awal


<img width="337" height="177" alt="Screenshot 2026-05-04 213648" src="https://github.com/user-attachments/assets/5e8f4bc8-b894-4481-bcbd-1da037e2ee67" />
Output data belum terurut 


<img width="519" height="165" alt="Screenshot 2026-05-04 213655" src="https://github.com/user-attachments/assets/68206b94-7395-4b4b-92c2-c35fbd0cf49c" />
Output data sudah terurut

<img width="508" height="67" alt="Screenshot 2026-05-04 213702" src="https://github.com/user-attachments/assets/bde57c4b-9a42-44a2-bb06-c441c76a102c" />
Output ketikan user menginputkan selain angka.

## Link Youtube
https://youtu.be/43A9UklWQ8c


























