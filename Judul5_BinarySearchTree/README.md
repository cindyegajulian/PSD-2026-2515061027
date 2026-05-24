# Sistem Pencatatan Nilai Ujian
## Deskripsi Singkat
Program ini berfungsi membantu guru mencatat dan mengelola nilai ujian siswa secara efisien. Melalui menu sederhana, guru dapat memasukkan nilai, mencari nilai tertentu, melihat pencapaian terendah (Min) dan tertinggi (Max), serta menghitung jumlah siswa dan total keseluruhan nilai untuk keperluan evaluasi seperti menghitung rata-rata kelas.

Secara teknis, program ini menerapkan struktur data Binary Search Tree (BST). Data nilai disusun secara hierarkis: nilai yang lebih kecil ditempatkan di cabang kiri node, dan yang lebih besar di cabang kanan. Pendekatan ini membuat proses penambahan (Insert) dan pencarian (Search) data menjadi sangat cepat. Program ini juga menggunakan Inorder Traversal untuk mencetak seluruh nilai siswa agar otomatis terurut dari yang paling kecil hingga paling besar.
