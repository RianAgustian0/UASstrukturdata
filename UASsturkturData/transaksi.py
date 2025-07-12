import csv

NAMA_FILE = 'transaksi.csv'

kategori_pemasukan = ["gaji", "ortu", "lain"]
kategori_pengeluaran = ["makan", "transportasi", "lain"]

def tambah_transaksi():
    print("\n--- Tambah Transaksi ---")
    print("1. Pemasukan")
    print("2. Pengeluaran")
    print("3. Kembali")
    pilih = input("Pilih (1-3): ")

    if pilih == "1":
        jenis = "pemasukan"
        print("Kategori: ", kategori_pemasukan)
        kategori = input("Masukkan kategori: ").lower()
        if kategori not in kategori_pemasukan:
            print("Kategori tidak valid!")
            return
    elif pilih == "2":
        jenis = "pengeluaran"
        print("Kategori: ", kategori_pengeluaran)
        kategori = input("Masukkan kategori: ").lower()
        if kategori not in kategori_pengeluaran:
            print("Kategori tidak valid!")
            return
    else:
        return

    tanggal = input("Tanggal (Tahun-Bulan-Tanggal): ")
    jumlah = input("Jumlah uang: ")
    if not jumlah.isdigit():
        print("Jumlah harus angka!")
        return

    with open(NAMA_FILE, 'r') as f:
        reader = list(csv.reader(f))
        id_baru = len(reader)

    with open(NAMA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([id_baru, tanggal, jenis, kategori, jumlah])
    print(" Transaksi ditambahkan!")