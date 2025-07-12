import csv
from transaksi import NAMA_FILE

def cek_laporan():
    print("\n--- Cek Transaksi ---")
    print("1. Laporan Bulanan")
    print("2. Laporan Tahunan")
    print("3. Lihat Semua Transaksi")
    print("4. Cek Berdasarkan Kategori")
    print("5. Kembali")
    pilih = input("Pilih (1-5): ")

    if pilih == "1":
        bulan = input("Masukkan bulan (01-12): ")
        tahun = input("Masukkan tahun (Tahun): ")
        total_masuk = 0
        total_keluar = 0
        with open(NAMA_FILE, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['tanggal'][5:7] == bulan and row['tanggal'][:4] == tahun:
                    if row['jenis'] == 'pemasukan':
                        total_masuk += int(row['jumlah'])
                    else:
                        total_keluar += int(row['jumlah'])
        print(f"\n{bulan}-{tahun}")
        print(f"Pemasukan: Rp{total_masuk}")
        print(f"Pengeluaran: Rp{total_keluar}")

    elif pilih == "2":
        tahun = input("Masukkan tahun (Tahun): ")
        total_masuk = 0
        total_keluar = 0
        with open(NAMA_FILE, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['tanggal'][:4] == tahun:
                    if row['jenis'] == 'pemasukan':
                        total_masuk += int(row['jumlah'])
                    else:
                        total_keluar += int(row['jumlah'])
        print(f"\nTahun {tahun}")
        print(f"Pemasukan: Rp{total_masuk}")
        print(f"Pengeluaran: Rp{total_keluar}")

    elif pilih == "3":
        print("\n=== Semua Transaksi ===")
        with open(NAMA_FILE, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"ID: {row['id']} | Tanggal: {row['tanggal']} | Jenis: {row['jenis']} | Kategori: {row['kategori']} | Jumlah: Rp{row['jumlah']}")

    elif pilih == "4":
        kategori_dicari = input("Masukkan kategori yang ingin dicek: ").lower()
        ditemukan = False
        print(f"\n=== Transaksi dengan Kategori: {kategori_dicari} ===")
        with open(NAMA_FILE, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['kategori'].lower() == kategori_dicari:
                    print(f"ID: {row['id']} | Tanggal: {row['tanggal']} | Jenis: {row['jenis']} | Jumlah: Rp{row['jumlah']}")
                    ditemukan = True
        if not ditemukan:
            print("Tidak ada transaksi dengan kategori tersebut.")

    else:
        return
