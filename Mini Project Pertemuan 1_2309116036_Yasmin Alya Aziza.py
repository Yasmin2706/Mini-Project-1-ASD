# Nama : Yasmin Alya Aziza
# NIM : 2309116036
# Kelas: Sistem Informasi A

# Program Pendataan Pemesanan Produk Tas

from prettytable import PrettyTable

# Class Pemesanan Produk Tas
class PemesananTas:
    def __init__(self, id_pesanan, nama_pelanggan, jenis_tas, jumlah_pesanan, total_harga):
        self.id_pesanan = id_pesanan
        self.nama_pelanggan = nama_pelanggan
        self.jenis_tas = jenis_tas
        self.jumlah_pesanan = jumlah_pesanan
        self.total_harga = total_harga

# Class Data Pemesanan Tas
class DataPemesanan:
    # Membuat kelas DataPemesanan yang memiliki atribut data_pesanan, yaitu kamus (dictionary) untuk menyimpan objek PemesananTas
    def __init__(self):
        self.data_pesanan = {}

    # Menambah data pesanan
    def tambah_pesanan(self, pesanan):
        self.data_pesanan[pesanan.id_pesanan] = pesanan

    # Melihat data pesanan
    def lihat_pesanan(self):
        if not self.data_pesanan:
            print("Belum ada pesanan yang masuk.")
        else:
            table = PrettyTable()
            table.field_names = ["ID Pesanan", "Nama Pelanggan", "Jenis Tas", "Jumlah Pesanan", "Total Harga"]

            for id_pesanan, pesanan in self.data_pesanan.items():
                table.add_row([id_pesanan, pesanan.nama_pelanggan, pesanan.jenis_tas, pesanan.jumlah_pesanan, pesanan.total_harga])

            print(table)

    # Menghapus data pesanan
    def hapus_pesanan(self, id_pesanan):
        if id_pesanan in self.data_pesanan:
            del self.data_pesanan[id_pesanan]
            print(f"Pesanan dengan ID {id_pesanan} berhasil dihapus.")
        else:
            print(f"Tidak ditemukan pesanan dengan ID {id_pesanan}. Masukkan ID yang tersedia.")

    # Memperbarui data pesanan
    def update_pesanan(self, id_pesanan, nama_pelanggan, jenis_tas, jumlah_pesanan, total_harga):
        if id_pesanan in self.data_pesanan:
            pesanan = self.data_pesanan[id_pesanan]
            pesanan.nama_pelanggan = nama_pelanggan
            pesanan.jenis_tas = jenis_tas
            pesanan.jumlah_pesanan = jumlah_pesanan
            pesanan.total_harga = total_harga
            print(f"Pesanan dengan ID {id_pesanan} berhasil diperbarui.")
        else:
            print(f"Tidak ditemukan pesanan dengan ID {id_pesanan}. Masukkan ID yang tersedia.")

# Membuat objek DataPemesanan
data_pemesanan = DataPemesanan()

while True:
    print("""
            ==================================================
            |                                                |
            |                BEAUTIFUL BAG                   |
            |            Pendataan Pemesanan Tas             |
            |                                                |
            ==================================================
            |                WELCOME HOME~                   |
            |  Silakan pilih pendataan yang ingin dipilih~   |
            -------------------------------------------------|
            |    Pendataan Pemesanan Tas Pelanggan:          |
            |    1. Tambah Pesanan                           |
            |    2. Lihat Pesanan                            |
            |    3. Hapus Pesanan                            |
            |    4. Update Pesanan                           |
            |    5. Keluar                                   |
            --------------------------------------------------
            """)

    pilihan = input("Pilih pendataan pemesanan tas pelanggan (1/2/3/4/5): ")

    if pilihan == "1":
        id_pesanan = int(input("Masukkan ID Pesanan (berupa angka): "))
        nama_pelanggan = input("Masukkan Nama Pelanggan: ")
        jenis_tas = input("Masukkan Jenis Tas (Slingbag/Totebag/Backpack): ")
        jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
        total_harga = float(input("Masukkan Total Harga: "))

        pesanan_baru = PemesananTas(id_pesanan, nama_pelanggan, jenis_tas, jumlah_pesanan, total_harga)
        data_pemesanan.tambah_pesanan(pesanan_baru)
        print("Pesanan telah berhasil ditambahkan.")

    elif pilihan == "2":
        print("\nDaftar Pesanan Tas Pelanggan:")
        data_pemesanan.lihat_pesanan()

    elif pilihan == "3":
        id_hapus = int(input("Masukkan ID Pesanan yang akan dihapus: "))
        data_pemesanan.hapus_pesanan(id_hapus)

    elif pilihan == "4":
        id_update = int(input("Masukkan ID Pesanan yang akan diupdate: "))
        nama_pelanggan = input("Masukkan Nama Pelanggan baru: ")
        jenis_tas = input("Masukkan Jenis Tas baru (Slingbag/Totebag/Backpack): ")
        jumlah_pesanan = int(input("Masukkan Jumlah Pesanan baru: "))
        total_harga = float(input("Masukkan Total Harga baru: "))

        data_pemesanan.update_pesanan(id_update, nama_pelanggan, jenis_tas, jumlah_pesanan, total_harga)

    elif pilihan == "5":
        print("""
            ==================================================
            |  Pendataan Pemesanan Produk Tas Telah Selesai. |
            |           Sampai Bertemu Kembali~.             |
            ==================================================
            """)
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5.")
