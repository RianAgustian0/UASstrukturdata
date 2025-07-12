import csv
from transaksi import NAMA_FILE

def edit_transaksi():
    print("\n=== Daftar Transaksi ===")
    with open(NAMA_FILE, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        for row in data:
            print(f"ID: {row['id']} | Tanggal: {row['tanggal']} | Jenis: {row['jenis']} | Kategori: {row['kategori']} | Jumlah: Rp{row['jumlah']}")

    id_target = input("\nMasukkan ID transaksi yang ingin diedit: ")

    for row in data:
        if row['id'] == id_target:
            print("\n--- Edit Transaksi ---")
            print("1. Tanggal")
            print("2. Jumlah Uang")
            print("3. Kategori")
            print("4. Jenis Transaksi")
            print("5. Keluar")
            opsi = input("Pilih bagian yang ingin diubah (1-5): ")

            if opsi == "1":
                row['tanggal'] = input("Tanggal baru (Tahun-Bulan-Tanggal): ")
            elif opsi == "2":
                row['jumlah'] = input("Jumlah baru: ")
            elif opsi == "3":
                row['kategori'] = input("Kategori baru: ")
            elif opsi == "4":
                row['jenis'] = input("Jenis baru (pemasukan/pengeluaran): ")
            else:
                return

            with open(NAMA_FILE, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['id', 'tanggal', 'jenis', 'kategori', 'jumlah'])
                writer.writeheader()
                writer.writerows(data)
            print("Transaksi berhasil diperbarui.")
            return

    print("ID tidak ditemukan.")
