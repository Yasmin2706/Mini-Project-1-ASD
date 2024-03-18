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

    # JUMP SEARCH (Mencari pesanan dengan fitur searching)
    # Mencari dengan id_pesanan
    def jumpSearch_idpesanan(self, id_pesanan):
        if not self.linked_list.head:
            print("Tidak ada pesanan yang bisa dicari karena data kosong.")
            return None
        
        # Menghitung jumlah total elemen dalam linked list
        total_elemen = 0
        current_node = self.linked_list.head
        while current_node:
            total_elemen += 1
            current_node = current_node.next
        
        # Menentukan ukuran blok untuk melakukan jump
        ukuran_blok = int(total_elemen ** 0.5)

        current_node = self.linked_list.head
        prev_node = None

        # Melakukan lompatan ke depan hingga ditemukan blok yang mungkin mengandung elemen yang ingin dicari
        while current_node and current_node.pesanan.id_pesanan < id_pesanan:
            prev_node = current_node
            for i in range(min(ukuran_blok, total_elemen)):
                if current_node.next:
                    current_node = current_node.next
                else:
                    break

        # Melakukan pencarian linear di dalam blok yang telah ditemukan
        while prev_node:
            if prev_node.pesanan.id_pesanan == id_pesanan:
                return prev_node.pesanan
            prev_node = prev_node.next

        # Melanjutkan pencarian secara linear dari current_node jika masih tidak ditemukan di dalam blok
        while current_node:
            if current_node.pesanan.id_pesanan == id_pesanan:
                return current_node.pesanan
            current_node = current_node.next

        # Jika tidak ditemukan
        print(f"Tidak ditemukan pesanan dengan ID {id_pesanan}.")
        return None
    
    # Mencari dengan jenis_tas
    def jumpSearch_jenistas(self, jenis_tas):
        if not self.linked_list.head:
            print("Tidak ada pesanan yang bisa dicari karena data kosong.")
            return None
            
        # Menghitung jumlah total elemen dalam linked list
        total_elemen = 0
        current_node = self.linked_list.head
        while current_node:
            total_elemen += 1
            current_node = current_node.next
            
        # Menentukan ukuran blok untuk melakukan jump
        ukuran_blok = int(total_elemen ** 0.5)

        current_node = self.linked_list.head
        hasil_pencarian = []

        # Melakukan lompatan ke depan hingga ditemukan blok yang mungkin mengandung elemen yang ingin dicari
        while current_node and current_node.pesanan.jenis_tas < jenis_tas:
            for i in range(min(ukuran_blok, total_elemen)):
                if current_node.next:
                    current_node = current_node.next
                else:
                    break

        # Melakukan pencarian linear di dalam blok yang telah ditemukan
        while current_node and current_node.pesanan.jenis_tas == jenis_tas:
            hasil_pencarian.append(current_node.pesanan)
            current_node = current_node.next

        # Jika tidak ditemukan
        if not hasil_pencarian:
            print(f"Tidak ditemukan pesanan dengan jenis tas {jenis_tas}.")
            return None
        else:
            return hasil_pencarian

    # SORTING DATA PESANAN
    def merge_sort(self, list, key):
        if len(list) > 1:   # Memeriksa apakah panjang daftar (list) lebih dari 1. Jika tidak, maka tidak perlu dilakukan sorting.
            mid = len(list) // 2    # Menentukan indeks tengah dari daftar.
            left_half = list[:mid]  # Membagi daftar menjadi dua bagian, yaitu sebelah kiri dan kanan.
            right_half = list[mid:]

            self.merge_sort(left_half, key)
            self.merge_sort(right_half, key)

            i, j, k = 0, 0, 0

            while i < len(left_half) and j < len(right_half):   # Melakukan loop sampai salah satu dari bagian kiri atau kanan habis.
                if getattr(left_half[i].pesanan, key) < getattr(right_half[j].pesanan, key):    # Membandingkan nilai atribut pesanan dari kedua bagian berdasarkan key, yaitu ID_Pesanan  atau Nama_Pelanggan.
                    list[k] = left_half[i]  # Menyusun kembali daftar dengan memilih nilai dari bagian kiri atau kanan sesuai hasil perbandingan.
                    i += 1  # Menambahkan nilai indeks i dan j setelah menyusun satu elemen untuk menghindari duplikasi dan memindahkan pointer ke elemen selanjutnya.
                else:
                    list[k] = right_half[j]
                    j += 1
                k += 1  # Menambah nilai indeks k untuk menggeser tempat penyusunan.

            while i < len(left_half):   # Menyusun sisa elemen dari bagian kiri atau kanan yang belum terproses.
                list[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                list[k] = right_half[j]
                j += 1
                k += 1

    def sort_pesanan(self, key, urutan='ascending'):    # Metode ini menerima 2 parameter, yaitu key, menentukan kriteria perbandingan untuk sorting, dan urutan, menentukan urutan sorting.
        if not self.linked_list.head:
            print("Tidak ada pesanan untuk diurutkan.")
            return

        pesanan_list = []   # Membuat daftar kosong untuk menyimpan node-node pesanan.
        current_node = self.linked_list.head
        while current_node: # Mengiterasi melalui linked list dan menambahkan setiap node ke dalam pesanan_list.
            pesanan_list.append(current_node)
            current_node = current_node.next

        self.merge_sort(pesanan_list, key)  # Memanggil metode merge_sort untuk mengurutkan pesanan_list berdasarkan key.

        if urutan == 'descending':
            pesanan_list.reverse()

        sorted_table = PrettyTable()
        sorted_table.field_names = ["ID Pesanan", "Nama Pelanggan", "Jenis Tas", "Jumlah Pesanan", "Total Harga"]

        for node in pesanan_list:   # Mengiterasi melalui pesanan_list dan menambahkan setiap pesanan ke dalam tabel. 
            pesanan = node.pesanan
            sorted_table.add_row([pesanan.id_pesanan, pesanan.nama_pelanggan, pesanan.jenis_tas, pesanan.jumlah_pesanan, pesanan.total_harga])

        print(sorted_table)


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

pesanan1 = PemesananTas(12, "Jaehyuk", "Backpack", 2, 30000)
pesanan2 = PemesananTas(34, "Wonyoung", "Totebag", 1, 15000)
pesanan3 = PemesananTas(56, "Alice", "Slingbag", 3, 30000)

data_pemesanan.tambahpesanan_di_awal(pesanan1)
data_pemesanan.tambahpesanan_di_akhir(pesanan2)
data_pemesanan.tambahpesanan_di_akhir(pesanan3)

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
            |    5. Sorting Pesanan                          |
            |    6. Searching Pesanan                        |
            |    7. Keluar                                   |
            --------------------------------------------------
            """)

    pilihan = input("Pilih pendataan pemesanan tas pelanggan (1/2/3/4/5/6/7): ")

    if pilihan == "1":
        id_pesanan = int(input("Masukkan ID Pesanan (berupa angka): "))
        nama_pelanggan = input("Masukkan Nama Pelanggan: ")
        while True:
            jenis_tas = input("Masukkan Jenis Tas (Slingbag/Totebag/Backpack): ")
            if jenis_tas in ["Slingbag", "Totebag", "Backpack"]:
                break
            else:
                print("Jenis tas yang dimasukkan tidak valid. Atau perhatikan huruf besar kecilnya. Silakan masukkan kembali.")
        jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
        total_harga = int(input("Masukkan Total Harga: "))
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
            |                Menghapus Pesanan               |
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
        while True:
            jenis_tas = input("Masukkan Jenis Tas (Slingbag/Totebag/Backpack): ")
            if jenis_tas in ["Slingbag", "Totebag", "Backpack"]:
                break
            else:
                print("Jenis tas yang dimasukkan tidak valid. Atau perhatikan huruf besar kecilnya. Silakan masukkan kembali.")
        jumlah_pesanan = int(input("Masukkan Jumlah Pesanan baru: "))
        total_harga = int(input("Masukkan Total Harga baru: "))

        data_pemesanan.update_pesanan(id_update, nama_pelanggan, jenis_tas, jumlah_pesanan, total_harga)

    elif pilihan == "5":
        print("""\n
            ==================================================
            |               Pendataan Pemesanan              |
            |                 Sorting Pesanan                |
            --------------------------------------------------
            |   Pilih kriteria sorting:                      |
            |   1. ID Pesanan                                |
            |   2. Nama Pelanggan                            |
            ==================================================
            """)
        kriteria_sorting = input("\nPilih kriteria sorting (1/2): ")
        urutan_sorting = input("Pilih urutan sorting (ascending/descending): ")

        if urutan_sorting == "ascending" or urutan_sorting == "descending":
            if kriteria_sorting == "1":
                data_pemesanan.sort_pesanan('id_pesanan', urutan_sorting)
            elif kriteria_sorting == "2":
                data_pemesanan.sort_pesanan('nama_pelanggan', urutan_sorting)
            else:
                print("Kriteria sorting tidak valid.")
        else:
            print("Input urutan sorting tidak valid. Harap masukkan 'ascending' atau 'descending'.")

    elif pilihan == "6":
        print("""\n
            ==================================================
            |               Pendataan Pemesanan              |
            |                Searching Pesanan               |
            --------------------------------------------------
            |   Pilih kriteria searching:                    |
            |   1. ID Pesanan                                |
            |   2. Jenis Tas                                 |
            ==================================================
            """)
        kriteria_searching = input("\nPilih kriteria searching (1/2): ")

        if kriteria_searching == "1": 
            id_pesanan = int(input("Masukkan ID Pesanan yang ingin dicari: "))
            hasil_pencarian = data_pemesanan.jumpSearch_idpesanan(id_pesanan)
            if hasil_pencarian is not None:
                print(f"Pesanan dengan ID {id_pesanan} ditemukan.")
                print("Detail Pesanan:")
                detil_tabelid = PrettyTable()
                detil_tabelid.field_names = ["ID Pesanan", "Nama Pelanggan", "Jenis Tas", "Jumlah Pesanan", "Total Harga"]
                detil_tabelid.add_row([hasil_pencarian.id_pesanan, hasil_pencarian.nama_pelanggan, hasil_pencarian.jenis_tas, hasil_pencarian.jumlah_pesanan, hasil_pencarian.total_harga])
                print(detil_tabelid)
            else:
                print(f"Tidak ditemukan pesanan dengan ID {id_pesanan}.")
        elif kriteria_searching == "2":
            while True:
                jenis_tas = input("Masukkan Jenis Tas (Slingbag/Totebag/Backpack): ")
                if jenis_tas in ["Slingbag", "Totebag", "Backpack"]:
                    break
                else:
                    print("Jenis tas yang dimasukkan tidak valid. Atau perhatikan huruf besar kecilnya. Silakan masukkan kembali.")
            hasil_pencarian = data_pemesanan.jumpSearch_jenistas(jenis_tas)
            if hasil_pencarian is not None:
                print(f"Pesanan dengan jenis tas {jenis_tas} ditemukan.")
                print("Detail Pesanan:")
                detil_tabeljt = PrettyTable()
                detil_tabeljt.field_names = ["ID Pesanan", "Nama Pelanggan", "Jenis Tas", "Jumlah Pesanan", "Total Harga"]
                if isinstance(hasil_pencarian, list):
                    for pesanan in hasil_pencarian:
                        detil_tabeljt.add_row([pesanan.id_pesanan, pesanan.nama_pelanggan, pesanan.jenis_tas, pesanan.jumlah_pesanan, pesanan.total_harga])
                else:
                    detil_tabeljt.add_row([hasil_pencarian.id_pesanan, hasil_pencarian.nama_pelanggan, hasil_pencarian.jenis_tas, hasil_pencarian.jumlah_pesanan, hasil_pencarian.total_harga])
                print(detil_tabeljt)
            else:
                print(f"Tidak ditemukan pesanan dengan jenis tas {jenis_tas}.")
        else:
            print("Input pilihan kriteria searching tidak valid. Harap masukkan inputan yang valid (1/2).")

    elif pilihan == "7":
        print("""
            ==================================================
            |  Pendataan Pemesanan Produk Tas Telah Selesai. |
            |           Sampai Bertemu Kembali~.             |
            ==================================================
            """)
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, 5, 6, atau 7.")

