import mysql.connector

from time import sleep
db = mysql.connector.connect(
    host='localhost',
    user="root",
    password="",
    database='perpustakaan'
)
def exit_program():
    clear_screen()
    print("Tunggu Sebentar Program Akan Berhenti")
    sleep(1)
    print("\n3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("Terima kasih atas kunjungan anda, kami mohon maaf apabila ada ketidaknyamanan saat anda berkunjung di perpustakaan digital")
    exit()

    

def kembali_menu():
    print("Tekan [ENTER] Lagi Untuk Kembali Ke Menu Program")
    input( )
    menu()

def clear_screen():
    import os
    os.system("CLS")

def menu():
    clear_screen()

    print("SELAMAT DATANG DI PERPUSTAKAAN DIGITAL\n")
    print("Di bawah ini adalah daftar program: ")
    print("="*43)
    print("|{:^5}|{:^35}|".format("No", "Jenis Program"))
    print("="*43)
    print("|{:^5}|{:^35}|".format("1", "Daftar Buku"))
    print("-"*43)
    print("|{:^5}|{:^35}|".format("2", "Tambah Buku"))
    print("-"*43)
    print("|{:^5}|{:^35}|".format("3", "Daftar riwayat peminjaman"))
    print("-"*43)
    print("|{:^5}|{:^35}|".format("4", "Menambah Riwayat peminjaman"))
    print("-"*43)
    print("|{:^5}|{:^35}|".format("5", "Memperbarui Riwayat Peminjaman"))
    print("-"*43)
    print("|{:^5}|{:^35}|".format("6", "Keluar"))
    print("="*43)

    pilih = int(input("\nMasukan nomor program untuk memilih program yang akan dijalankan : "))
    if pilih == 1 : 
        display_buku()
    elif pilih == 2:
        add()
    elif pilih == 3:
        riwayat_pinjam()
    elif pilih == 4:
        tambah_peminjam()
    elif pilih == 5:
        update_riwayat_peminjaman()
    elif pilih == 6:
        exit_program()

def data_buku(kode_buku, judul_buku, penulis_buku, tahun_terbit):
    cursor = db.cursor()
    query = "INSERT INTO tb_buku (kode_buku, judul_buku, penulis_buku, tahun_terbit) VALUES (%s, %s, %s, %s)"
    values = (kode_buku, judul_buku, penulis_buku, tahun_terbit)
    
    cursor.execute(query, values)
    db.commit()

    print("Data berhasil ditambahkan.")

def fetch_buku():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_buku")
    return cursor.fetchall()

def display_buku():
    clear_screen()
    print("Daftar Buku Yang Tersedia Di Perpustakaan Digital : \n")
    print("="*84)
    print("|{:^5}|{:^8}|{:^25}|{:^25}|{:^15}|".format("No", "Kode", "Judul Buku", "Penulis", "Tahun Terbit"))
    print("="*84)
    items = fetch_buku()
    for item in items:
        print("|{:^5}|{:^8}|{:^25}|{:^25}|{:^15}|".format(item[0], item[1], item[2], item[3], item[4]))
        print("-"*84)
    kembali_menu()
            
def add():
    clear_screen()
    print("Anda Berada Di Halaman Program Tambah buku\n\n")
    print("Daftar Buku Yang Tersedia Di Perpustakaan Digital : \n")
    print("="*84)
    print("|{:^5}|{:^8}|{:^25}|{:^25}|{:^15}|".format("No", "Kode", "Judul Buku", "Penulis", "Tahun Terbit"))
    print("="*84)
    items = fetch_buku()
    for item in items:
        print("|{:^5}|{:^8}|{:^25}|{:^25}|{:^15}|".format(item[0], item[1], item[2], item[3], item[4]))
        print("-"*84)
    while True : 
        tambah_buku = input("\nApakah Anda Ingin Menambahan buku? [Y /N] : ").upper()
        if tambah_buku == "Y":
            kode_buku = input("\nMasukkan Kode Buku : ")
            judul_buku = input("Masukkan Judul Buku : ")
            penulis_buku = input("Masukkan Nama Penulis Buku : ")
            tahun_terbit = int(input("Masukkan Tahun Terbit Buku : "))
            data_buku(kode_buku, judul_buku, penulis_buku, tahun_terbit)
        elif tambah_buku == "N":
            kembali_menu()
        else:
            print("Input Yang Anda Masukan Tidak Valid!")

def data_pinjam(nama_peminjam, buku_dipinjam, tanggal_pinjam, tanggal_kembali):
    cursor = db.cursor()
    query = "INSERT INTO tb_peminjam (nama_peminjam, buku_dipinjam, tanggal_pinjam, tanggal_kembali) VALUES(%s, %s, %s, %s)"
    values = (nama_peminjam, buku_dipinjam, tanggal_pinjam, tanggal_kembali)

    cursor.execute(query, values)
    db.commit()

    print("\nData Peminjam Berhasil ditambahkan")

def fetch_peminjam():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_peminjam")
    return cursor.fetchall()

def riwayat_pinjam():
    clear_screen()
    print("Ini Adalah Daftar Riwayat Peminjam: \n")

    print("="*111)
    print("|{:^5}|{:^25}|{:^25}|{:^25}|{:^25}|".format("Id", "Nama Peminjam", "Buku Dipinjam", "Tanggal Pinjam", "Tanggal Kembali"))
    print("="*111)

    pj_data = fetch_peminjam()
    
    for pj_riwayat in pj_data:
        print("|{:^5}|{:^25}|{:^25}|{:^25}|{:^25}|".format(pj_riwayat[0], pj_riwayat[1], pj_riwayat[2], pj_riwayat[3], pj_riwayat[4]))
        print("-"*111)
    
    kembali_menu()

def tambah_peminjam():
    clear_screen()
    print("Anda Berada Di Halaman Program Tambah Data Peminjam \n")
    print("Ini Adalah Daftar Riwayat Peminjam: \n")

    print("="*111)
    print("|{:^5}|{:^25}|{:^25}|{:^25}|{:^25}|".format("Id", "Nama Peminjam", "Buku Dipinjam", "Tanggal Pinjam", "Tanggal Kembali"))
    print("="*111)

    pj_data = fetch_peminjam()
    
    for pj_riwayat in pj_data:
        print("|{:^5}|{:^25}|{:^25}|{:^25}|{:^25}|".format(pj_riwayat[0], pj_riwayat[1], pj_riwayat[2], pj_riwayat[3], pj_riwayat[4]))
        print("-"*111)
    while True : 
        menambah_peminjam = input("\nApakah Anda Ingin Menambahkan Data Peminjam? [Y /N] : ").upper()

        if menambah_peminjam == "Y":
            nama_peminjam = input("\nMasukkan Nama Peminjam : ")
            buku_dipinjam = input("Masukan Judul Buku Yang Dipinjam : ")
            tanggal_pinjam = input("Masukkan Tanggal Pinjam : ")
            tanggal_kembali = input("Masukkan Tanggal Kembali : ")
            data_pinjam(nama_peminjam, buku_dipinjam, tanggal_pinjam, tanggal_kembali)

        elif menambah_peminjam == "N":
            kembali_menu()

        else:
            print("Input Yang Anda Masukan Tidak Valid!")

def update_riwayat_peminjaman():
    clear_screen()
    print("Memperbarui Riwayat Peminjaman\n")

    print("Daftar Riwayat Peminjaman: \n")
    print("="*111)
    print("|{:^5}|{:^25}|{:^25}|{:^25}|{:^25}|".format("No", "Nama Peminjam", "Buku Dipinjam", "Tanggal Pinjam", "Tanggal Kembali"))
    print("="*111)
    pj_data = fetch_peminjam()
    for pj_riwayat in pj_data:
        print("|{:^5}|{:^25}|{:^25}|{:^25}|{:^25}|".format(pj_riwayat[0], pj_riwayat[1], pj_riwayat[2], pj_riwayat[3], pj_riwayat[4]))
        print("-"*111)


    try:
        id_peminjam = int(input("\nMasukkan ID peminjaman yang ingin diperbarui: "))
        tanggal_kembali_baru = input("Masukkan tanggal kembali baru : ")

        cursor = db.cursor()
        query = "UPDATE tb_peminjam SET tanggal_kembali = %s WHERE id = %s"
        values = (tanggal_kembali_baru, id_peminjam)
        cursor.execute(query, values)
        db.commit()

        print("\nTanggal kembali berhasil diperbarui.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    kembali_menu()



if __name__ == "__main__":
    menu()
