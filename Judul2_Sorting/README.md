# Sistem Mengurutkan Stok Barang di Koperasi
## Deskripsi Singkat
Program ini adalah aplikasi sederhana berbasis teks yang berfungsi untuk mencatat dan mengelola data stok barang di sebuah koperasi. Tujuan utama dari program ini adalah membantu petugas koperasi memantau persediaan dengan cara mengurutkan daftar barang secara otomatis dari jumlah stok yang paling sedikit hingga paling banyak. Dengan begitu, petugas bisa lebih cepat mengambil keputusan terkait barang apa saja yang perlu segera dipesan ulang (restock). 

Dalam penyelesaiannya, program ini mengimplementasikan algoritma pengurutan exchange sort untuk memproses pertukaran posisi data. Sementara itu, struktur data yang diterapkan adalah array satu dimensi (implementasinya menggunakan list) yang di dalamnya menampung objek dictionary agar pasangan data antara nama barang dan jumlah stoknya dapat tersimpan secara rapi dalam satu kesatuan.

Baris 1-4, membuat fungsi bernama tukar, pada baris kedua (temp = arr[i]) menyalin barang dari posisi i ke sebuah tempat bernama temp. 
