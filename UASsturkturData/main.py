from transaksi import tambah_transaksi
from cektransaksi import cek_laporan
from edittransaksi import edit_transaksi
from hapustransaksi import hapus_transaksi

def menu():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tambah Transaksi")
        print("2. Cek Transaksi")
        print("3. Edit Transaksi")
        print("4. Hapus Transaksi")
        print("5. Keluar")
        pilih = input("Pilih menu (1-5): ")

        if pilih == "1":
            tambah_transaksi()
        elif pilih == "2":
            cek_laporan()
        elif pilih == "3":
            edit_transaksi()
        elif pilih == "4":
            hapus_transaksi()
        elif pilih == "5":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid!")

menu()