def menu():
    print("\n--- Sistem Input Nilai Kuis Mahasiswa ---")
    print("1. Tampilkan lokasi memori arsip nilai (Address array)")
    print("2. Tampilkan lokasi memori slot nilai per mahasiswa (Address index)")
    print("3. Masukkan nilai kuis untuk 5 mahasiswa")
    print("4. Keluar")
    print("-----------------------------------------")

def main():
    nilai_mahasiswa = [0] * 5
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        if choice == 1:
            print(f"Lokasi memori arsip nilai (Array Address): {id(nilai_mahasiswa)}")
        elif choice == 2:
            for i in range(5):
                print(f"Lokasi memori nilai Mahasiswa {i+1} (Address index {i}): {id(nilai_mahasiswa[i])}")
        elif choice == 3:
            print("Masukkan nilai kuis untuk 5 mahasiswa:")
            for i in range(5):
                while True:
                    try:
                        nilai_mahasiswa[i] = int(input(f"Nilai Mahasiswa {i+1} (index {i}): "))
                        break
                    except ValueError:
                        print("Input tidak valid, silakan masukkan angka!")
            print(f"\nRekapitulasi Nilai Saat Ini: {nilai_mahasiswa}")
        elif choice == 4:
            running = False
            print("Data nilai tersimpan. Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()