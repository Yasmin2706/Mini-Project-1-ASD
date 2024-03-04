# Nama : Yasmin Alya Aziza
# NIM : 2309116036
# Kelas: Sistem Informasi A

# Program Pendataan Pemesanan Produk Tas
# LINKED LIST

from prettytable import PrettyTable

# Class Node untuk Linked List
class Node:
    def __init__(self, pesanan):
        self.pesanan = pesanan
        self.next = None

# Class Single Linked List
class LinkedList:
    def __init__(self):
        self.head = None

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
    def __init__(self):
        self.linked_list = LinkedList()

    # MENAMBAH DATA PESANAN
    # Menambah data pesanan di awal linked list
    def tambahpesanan_di_awal(self, pesanan):
        new_node = Node(pesanan)
        new_node.next = self.linked_list.head
        self.linked_list.head = new_node
    # Menambah data pesanan di akhir linked list
    def tambahpesanan_di_akhir(self, pesanan):
        new_node = Node(pesanan)
        if not self.linked_list.head:
            self.linked_list.head = new_node
            return
        last_node = self.linked_list.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    # Menambah data pesanan di antara dua node
    def tambahpesanan_di_antara(self, id_setelah, pesanan_baru):
        current_node = self.linked_list.head
        while current_node and current_node.pesanan.id_pesanan != id_setelah:
            current_node = current_node.next

        if current_node:
            pesanan_baru_node = Node(pesanan_baru)
            pesanan_baru_node.next = current_node.next
            current_node.next = pesanan_baru_node
            print("Pesanan berhasil ditambahkan setelah ID Pesanan yang ditentukan.")
        else:
            print(f"Tidak ditemukan pesanan dengan ID {id_setelah}. Proses penambahan dibatalkan.")

    # MELIHAT DATA PESANAN
    def lihat_pesanan(self):
        if not self.linked_list.head:
            print("Belum ada pesanan yang masuk.")
        else:
            table = PrettyTable()
            table.field_names = ["ID Pesanan", "Nama Pelanggan", "Jenis Tas", "Jumlah Pesanan", "Total Harga"]

            current_node = self.linked_list.head
            while current_node:
                pesanan = current_node.pesanan
                table.add_row([pesanan.id_pesanan, pesanan.nama_pelanggan, pesanan.jenis_tas, pesanan.jumlah_pesanan, pesanan.total_harga])
                current_node = current_node.next

            print(table)

    # MENGHAPUS DATA PESANAN
    # Menghapus data pesanan di awal linked list
    def hapus_pesanan_di_awal(self):
        if self.linked_list.head:
            deleted_id = self.linked_list.head.pesanan.id_pesanan
            self.linked_list.head = self.linked_list.head.next
            print(f"Pesanan dengan ID {deleted_id} berhasil dihapus di awal data.")
        else:
            print("Tidak ada pesanan yang bisa dihapus. Data kosong.")
    # Menghapus data pesanan di akhir linked list
    def hapus_pesanan_di_akhir(self):
        current_node = self.linked_list.head
        prev_node = None

        while current_node and current_node.next:
            prev_node = current_node
            current_node = current_node.next

        if prev_node:
            prev_node.next = None
        else:
            self.linked_list.head = None

        if current_node:
            deleted_id = current_node.pesanan.id_pesanan
            print(f"Pesanan dengan ID {deleted_id} berhasil dihapus di akhir data.")
        else: 
            print("Tidak ada pesanan yang bisa dihapus. Data kosong.")
    # Menghapus data pesanan di antara data
    def hapus_pesanan(self, id_pesanan):
        if id_pesanan is None:
            print("Anda harus memberikan ID Pesanan untuk penghapusan di antara data.")
            return
        if not self.linked_list.head:
            print("Tidak ada pesanan yang bisa dihapus. Data kosong.")
            return

        current_node = self.linked_list.head
        prev_node = None

        while current_node and current_node.pesanan.id_pesanan != id_pesanan:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            print(f"Tidak ditemukan pesanan dengan ID {id_pesanan}.")
            return

        if prev_node:
            prev_node.next = current_node.next
        else:
            self.linked_list.head = current_node.next

        print(f"Pesanan dengan ID {id_pesanan} berhasil dihapus.")

    # MEMPERBARUI DATA PESANAN
    def update_pesanan(self, id_pesanan, nama_pelanggan, jenis_tas, jumlah_pesanan, total_harga):
        current_node = self.linked_list.head
        while current_node and current_node.pesanan.id_pesanan != id_pesanan:
            current_node = current_node.next
        if current_node:
            pesanan = current_node.pesanan
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
        print("""\n
            ==================================================
            |               Pendataan Pemesanan              |
            |                Menambah Pesanan                |
            --------------------------------------------------
            |   Pada tambahan pesanan produk, di data mana   |
            |            yang ingin anda letakkan?           |
            | 1. Di awal data                                |
            | 2. Di akhir data                               |
            | 3. Di tengah-tengah data                       |
            ==================================================
            """)
        penambahan = input("\nPenambahan akan diletakkan pada (1/2/3): ")

        if penambahan == "1":
            pesanan_baru = PemesananTas(id_pesanan, nama_pelanggan, jenis_tas, jumlah_pesanan, total_harga)
            data_pemesanan.tambahpesanan_di_awal(pesanan_baru)
            print("Pesanan telah berhasil ditambahkan.")

        elif penambahan == "2":
            pesanan_baru = PemesananTas(id_pesanan, nama_pelanggan, jenis_tas, jumlah_pesanan, total_harga)
            data_pemesanan.tambahpesanan_di_akhir(pesanan_baru)
            print("Pesanan telah berhasil ditambahkan.")

        elif penambahan == "3":
            id_setelah = int(input("Masukkan ID Pesanan untuk menambah data setelah ID Pesanan yang telah dimasukkan: "))
            pesanan_baru = PemesananTas(id_pesanan, nama_pelanggan, jenis_tas, jumlah_pesanan, total_harga)
            data_pemesanan.tambahpesanan_di_antara(id_setelah, pesanan_baru)

        else:
            print("Anda tidak memasukkan input yang benar. Proses selanjutnya akan kembali ke menu utama.")

    elif pilihan == "2":
        print("\nDaftar Pesanan Tas Pelanggan:")
        data_pemesanan.lihat_pesanan()

    elif pilihan == "3":
        print("""\n
            ==================================================
            |               Pendataan Pemesanan              |
            |                Menambah Pesanan                |
            --------------------------------------------------
            |         Pada penghapusan pesanan produk,       |
            |         pesanan mana yang ingin dihapus?       |
            | 1. Di awal data                                |
            | 2. Di akhir data                               |
            | 3. Di tengah-tengah data                       |
            ==================================================
            """)
        penghapusan = input("\nPenghapusan data akan dilakukan di (1/2/3): ")

        if penghapusan == "1":            
            data_pemesanan.hapus_pesanan_di_awal()
        
        elif penghapusan == "2":            
            data_pemesanan.hapus_pesanan_di_akhir()

        elif penghapusan == "3":            
            id_hapus_tengah = int(input("Masukkan ID Pesanan yang akan dihapus di antara data: "))
            data_pemesanan.hapus_pesanan(id_hapus_tengah)

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
