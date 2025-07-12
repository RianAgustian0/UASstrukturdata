import csv
from transaksi import NAMA_FILE

def hapus_transaksi():
    print("\n=== Daftar Transaksi ===")
    with open(NAMA_FILE, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        for row in data:
            print(f"ID: {row['id']} | Tanggal: {row['tanggal']} | Jenis: {row['jenis']} | Kategori: {row['kategori']} | Jumlah: Rp{row['jumlah']}")

    id_target = input("\nMasukkan ID transaksi yang ingin dihapus: ")
    data_baru = [row for row in data if row['id'] != id_target]

    if len(data) == len(data_baru):
        print("Maaf, ID tidak ditemukan.")
        return

    with open(NAMA_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'tanggal', 'jenis', 'kategori', 'jumlah'])
        writer.writeheader()
        writer.writerows(data_baru)

    print("Transaksi berhasil dihapus.")
