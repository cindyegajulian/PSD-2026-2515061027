# Sistem Mengurutkan Stok Barang di Koperasi
## Deskripsi Singkat
Program ini adalah aplikasi sederhana berbasis teks yang berfungsi untuk mencatat dan mengelola data stok barang di sebuah koperasi. Tujuan utama dari program ini adalah membantu petugas koperasi memantau persediaan dengan cara mengurutkan daftar barang secara otomatis dari jumlah stok yang paling sedikit hingga paling banyak. Dengan begitu, petugas bisa lebih cepat mengambil keputusan terkait barang apa saja yang perlu segera dipesan ulang (restock). 

Dalam penyelesaiannya, program ini mengimplementasikan algoritma pengurutan exchange sort untuk memproses pertukaran posisi data. Sementara itu, struktur data yang diterapkan adalah array satu dimensi (implementasinya menggunakan list) yang di dalamnya menampung objek dictionary agar pasangan data antara nama barang dan jumlah stoknya dapat tersimpan secara rapi dalam satu kesatuan.

Baris 1-4, membuat fungsi bernama tukar, pada baris kedua (temp = arr[i]) menyalin barang dari posisi i ke sebuah tempat bernama temp. Baris ketiga mengisi posisi i dengan barang dari posisi j. Baris keempat mengambil barang yang tadi diletakkan di temp, lalu menaruhnya di posisi j.

Baris 6 membuat fungsi utama untuk mengurutkan barang, tempat dimana program akan berjalan untuk menyelesaikan studi kasus ini, dengan arr (daftar barang) dan n (jumlah total barang).

Baris 7 yaitu melakukan perulangan, kenapa n - 1? karena yang akan dibandingkan tidak semua elemen maka dari itu n - 1, jika elemen sudah terurut otomatis elemen paling akhir adalah elemen terbesar jadi tidak perlu di bandingkan lagi.

Baris ke 8 yaitu melakukan perulangan kedua, disini akan mengecek sisa barang lain yang ada di sebelah kanan dari posisi i. Maka dari itu dia i + 1.

Pada baris 9 dan 10 yaitu dilakukan pengecekan apakah jumlah stok di posisi kiri (i) lebih besar dari stok di posisi kanan (j). Jika iya, akan di tukar agar barang yang stoknya sisa sedikit berpindah ke sebelah kiri.

Baris 12 dan 13 def(main) ibarat tempat dimana program akan mulai jalan dari sini. lalu try, program mencoba menjalankan perintah dibawahnya, disini juga antisipasi kalau nanti ada error.

Baris 14 memunculkan teks pertanyaan di layar, lalu mengubah jawaban yang diketik menjadi angka bulat (int) dan menyimpannya di huruf n.

Baris 15 dan 16 jika ternyata yang diketik bukan angka (misalnya huruf "A"), program menangkap error tersebut di sini. Dan return menampilkan pesan bahwa input salah, lalu return langsung menghentikan program agar tidak error.

Baris 18 dan 19 membuat sebuah daftar kosong bernama arr untuk menyimpan semua data barang nanti. Lalu mencetak tulisan ke layar. 

Baris 20 melakukan perulangan untuk meminta data barang baru sebanyak n kali.





















