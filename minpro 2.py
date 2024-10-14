from prettytable import PrettyTable

users = [
    {"Username": "Azhaar Athahiroh", "Password": "Sepuluh", "Role": "Admin"}
]

cooking_class = [
    {"Kode Kelas": 1, "Nama Kelas": "Bebek Goreng", "Harga": 180000, "Jadwal": "Senin", "Slot": 6},
    {"Kode Kelas": 2, "Nama Kelas": "Ayam Woku", "Harga": 165000, "Jadwal": "Rabu", "Slot": 5},
    {"Kode Kelas": 3, "Nama Kelas": "Ramen", "Harga": 200000, "Jadwal": "Kamis", "Slot": 5},
    {"Kode Kelas": 4, "Nama Kelas": "Sempol Ayam", "Harga": 145000, "Jadwal": "Jumat", "Slot": 7},
    {"Kode Kelas": 5, "Nama Kelas": "Nasi Goreng Italy", "Harga": 180000, "Jadwal": "Sabtu", "Slot": 5}
]

def login():
    print("=== Jasa Cooking Class ===")
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user["Username"] == username and user["Password"] == password:
            print(f"Login berhasil! Selamat datang, {user["Role"]}")
        else:
            print("Username atau password salah!")    
    pilih_role()


def pilih_role ():
    
    print("Anda adalah :")
    print("1. Admin")
    print("2. Pembeli")
    opsi = int(input("Masukkan pilihan anda : "))
    if  opsi == 1:
        menu_admin()
    elif opsi == 2:
        menu_pembeli()
    else:
        print("Pilihan anda tidak ada")

def tampilkan_kelas():
    table = PrettyTable(["Kode Kelas", "Nama Kelas", "Harga", "Jadwal", "Slot"])
    for kelas in cooking_class:
        table.add_row([kelas["Kode Kelas"], kelas["Nama Kelas"], kelas["Harga"], kelas["Jadwal"], kelas["Slot"]])
    print(table)

def tambahkan_kelas():
    print("\n=== Tambahkan Kelas ===")
    kode_kelas = int(input("Masukkan Kode Kelas: "))
    nama_kelas = input("Masukkan Nama Kelas: ")
    harga = int(input("Masukkan Harga: "))
    jadwal = input("Masukkan Jadwal: ")
    slot = int(input("Masukkan Slot Kelas: "))
    cooking_class.append({"Kode Kelas": kode_kelas, "Nama Kelas": nama_kelas, "Harga": harga, "Jadwal": jadwal, "Slot": slot})
    print(f"Kelas {nama_kelas} dengan kode {kode_kelas} berhasil ditambahkan")

def hapus_kelas():
    print("\n=== Hapus kelas ===")
    kode_hapus = int(input("Masukkan Kode Kelas yang ingin dihapus: "))
    for kelas in cooking_class:
        if kelas["Kode Kelas"] == kode_hapus:
            cooking_class.remove(kelas)
            print(f"Kelas dengan kode {kode_hapus} berhasil dihapus")
            return
    print(f"Kelas dengan kode {kode_hapus} tidak ditemukan")

def transaksi_pembeli():
    print("\n=== Daftar Kelas Memasak ===")
    tampilkan_kelas()
    kode_pilih = int(input("Masukkan Kode Kelas yang ingin diikuti: "))
    for kelas in cooking_class:
        if kelas["Kode Kelas"] == kode_pilih:
            if kelas["Slot"] > 0:
                kelas["Slot"] -= 1
                print(f"Anda berhasil mendaftar ke kelas {kelas['Nama Kelas']} pada hari {kelas['Jadwal']} Slot tersisa: {kelas['Slot']}")
            else:
                print(f"Maaf kelas {kelas['Nama Kelas']} sudah penuh")
            return
    print("Kode kelas tidak valid")

def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tampilkan Kelas")
        print("2. Tambahkan Kelas")
        print("3. Hapus Kelas")
        print("4. Logout")
        pilihan = input("Pilih Opsi: ")
        if pilihan == "1":
            tampilkan_kelas()
        elif pilihan == "2":
            tambahkan_kelas()
        elif pilihan == "3":
            hapus_kelas()
        elif pilihan == "4":
            print("Logout berhasil")
            break
        else:
            print("Pilihan tidak valid")

def menu_pembeli():
    while True:
        print("\n=== Menu Pembeli ===")
        print("1. Tampilkan Kelas")
        print("2. Daftar Kelas Memasak")
        print("3. Logout")
        pilihan = input("Pilih Opsi: ")
        if pilihan == "1":
            tampilkan_kelas()
        elif pilihan == "2":
            transaksi_pembeli()
        elif pilihan == "3":
            print("Logout berhasil")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    login()