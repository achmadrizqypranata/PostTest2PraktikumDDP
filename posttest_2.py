# Program Figure Shop (2 Login Spesifik, CRUD, dan menu transaksi)
# Achmad Rizqy Pranata (2209116086)

def login_admin():
    username = "admin"
    password = "admin"
    while True:
        username_ = input("Masukkan Username Anda: ")
        password_ = input("Masukkan Password Anda: ") 
        if password_ == password and username_ == username:
            print("-------------------------------------------------------")
            print("Selamat Datang di Dashboard Violet Figure Shop")
            print("-------------------------------------------------------")
            break
        else:
            print("Login Anda ditolak, Silahkan Coba lagi\n")


def login_pembeli():

    while True:
        print("-------------------------------------------------------")
        print("Selamat Datang di Violet Figure Shop")
        print("-------------------------------------------------------")
        name = input("Masukkan Nama Anda: ")
        password = input("Buat Password Anda: ")
        confirmPass = input("Masukkan Password Anda: ")  
        if password == confirmPass:
            print("-------------------------------------------------------")
            print("Selamat berkhilaf UwU")
            print("-------------------------------------------------------")
            break
        else:
            print("Login Gagal, Silahkan Coba lagi\n")



coverstrip = '-'*55

DaftarBarang = ["PVC Figure 1/7 Special Week - Uma Musume : Pretty Derby", "PVC Figure 1/7 Anya Forger & Bond Forger - SPY x FAMILY", "Ichiban Kuji Figure Midoriya Izuku - Boku no Hero Academia -Ishi- A Prize", "Glitter & Glamours Figure Super Sailor Neptune - Pretty Guardian Sailor Moon Eternal The Movie (25cm)", "PVC Figure 1/7 Caster / Altria Caster - 2nd Ascension",]
Figure = ["PVC Figure 1/7 Special Week - Uma Musume : Pretty Derby", "PVC Figure 1/7 Anya Forger & Bond Forger - SPY x FAMILY", "Ichiban Kuji Figure Midoriya Izuku - Boku no Hero Academia -Ishi- A Prize", "Glitter & Glamours Figure Super Sailor Neptune - Pretty Guardian Sailor Moon Eternal The Movie (25cm)", "PVC Figure 1/7 Caster / Altria Caster - 2nd Ascension",]

def admin_toko():
    #Login sebagai Admin

    loop = True     
    while loop:
        print("1. Cetak Data Barang")
        print("2. Tambah Data Barang")
        print("3. Hapus Data Barang")
        print("4. Ubah Data Barang")
        print("5. Exit")
        print(coverstrip)         
        choice = int(input("Silahkan pilih menu (1-5): "))
        print()
     
        if choice==1:     
            print("Menu 1 telah dipilih")
            c1 = input("Anda yakin ingin mencetak daftar barang (Y/N)? ")
            c1 = c1.lower()
            if c1 == "y" and DaftarBarang != []:
                print(DaftarBarang)
            elif DaftarBarang == []:
                print("Daftar Barang Kosong")
            else:
                c2 = input("Ingin kembali ke menu (Y/N)? ")
                c2 = c2.lower()
                if c2 == "y":
                    loop = True
                else:
                    print("Terima Kasih !")
                    loop = False
                    print()        
        elif choice==2:
            print("Menu 2 telah dipilih")
            cekdata = input("Silahkan masukkan data yang akan ditambahkan : ")
            cekdata = cekdata.lower()
            for i in Figure:
                if cekdata in Figure:
                    if cekdata in DaftarBarang:
                        m = input("Data sudah ada dalam list, tetap ditambahkan (Y/N)?")
                        m = m.lower()
                        if m == "y":
                            DaftarBarang.append(cekdata)
                            print("Data telah ditambahkan")
                            print(DaftarBarang)
                            break
                        else:
                            print("Data Tidak Ditambahkan")
                    else:
                        DaftarBarang.append(cekdata)
                        print("Data telah Ditambahkan")
                        print(DaftarBarang)
                        break    
                else: 
                    print("Data yang Anda masukkan bukan figure")
                break
        elif choice==3:
            print("Menu 3 telah dipilih")
            print(f"Berikut adalah daftar barang anda : {DaftarBarang}")
            print("""1. Hapus sebagian data\n2. Hapus seluruh data""")
            deldaftar = input("Pilih menu untuk menghapus list : ")
            if deldaftar == "1":
                try:
                    pildata = input("Masukan nama barang yang ingin dihapus : ")
                    pildata = pildata.lower()
                    for a in DaftarBarang:
                        DaftarBarang.remove(pildata)
                        print("Data telah di hapus")
                        print(DaftarBarang)
                        break
                except:
                    print(f"{pildata} tidak ada dalam daftar")
            elif deldaftar == "2":
                jwb = input("Anda yakin ingin menghapus seluruhnya (Y/N)?")
                jwb = jwb.lower()
                if jwb == "y":
                    DaftarBarang.clear()
                    print("Data dihapus seluruhnya")
                    print(f"Daftar barang anda adalah : {DaftarBarang}")
                else:
                    print("Data tidak dihapus")
            else:
                print("Angka tidak ada dalam pilihan")
        elif choice==4:
            print("Menu 4 telah dipilih")
            print(f"Berikut daftar barang anda : {DaftarBarang}")
            run = True
            while run:
                try:
                    datalama = input("Silahkan masukan nama barang yg ingin di ubah : ")
                    datalama = datalama.lower()
                    for w in DaftarBarang:
                        if datalama not in DaftarBarang:
                            print("Nama barang yang ingin anda ubah tidak ada")
                        else:
                            databaru = input("Silahkan masukan data barang baru : ")
                            databaru = databaru.lower()
                            indatalama = DaftarBarang.index(datalama)
                            DaftarBarang[indatalama] = databaru
                            print(DaftarBarang)
                            print("Data Berhasil Diubah")
                            run = False
                        break
                except:
                    print("Nama barang salah")
        elif choice==5:
            print("Thank you and see you XD")
            loop = False
        else:
            input("Pilihan tidak ada di menu, coba lagi!")

def pembeli_toko():
    #Login sebagai Pembeli
    from prettytable import PrettyTable 

    coverstrip = '-'*55
    
    print("List Daftar Figure")
    table = PrettyTable()
    table.field_names = ["No", "Nama Figure", "Harga"]
    table.add_row([1, "PVC Figure 1/7 Special Week - Uma Musume : Pretty Derby", "Rp 3.150.000"])
    table.add_row([2, "PVC Figure 1/7 Anya Forger & Bond Forger - SPY x FAMILY", "Rp 2.550.000"])
    table.add_row([3, "Ichiban Kuji Figure Midoriya Izuku - Boku no Hero Academia -Ishi- A Prize", "Rp 980.000"])
    table.add_row([4, "Glitter & Glamours Figure Super Sailor Neptune - Pretty Guardian Sailor Moon Eternal The Movie (25cm)", "Rp 320.000"])
    table.add_row([5, "PVC Figure 1/7 Caster / Altria Caster - 2nd Ascension ", "Rp 3.450.000"])
    print(table)
    listFigure=str(input(" Masukkan angka sesuai dengan figure yang tersedia = "))
    jumlah=int(input(" Jumlah dibeli (unit) = "))
    if listFigure == "1":
        namaFigure= " PVC Figure 1/7 Special Week - Uma Musume : Pretty Derby "
        harga=(3150000*jumlah)
        pajak= int(harga * 0.1)
        if jumlah >= 5:
            totalHarga=int(harga+pajak)
        else:
            totalHarga=int(harga+pajak)
    elif listFigure == "2":
        namaFigure= " PVC Figure 1/7 Anya Forger & Bond Forger - SPY x FAMILY "
        harga = (2550000*jumlah)
        pajak = int(harga * 0.1)
        if jumlah >= 5:
            totalHarga =int(harga+pajak)
        else:
            totalHarga =int(harga+pajak)
    elif listFigure == "3":
        namaFigure= " Ichiban Kuji Figure Midoriya Izuku - Boku no Hero Academia -Ishi- A Prize "
        harga=int(980000*jumlah)
        pajak = int(harga * 0.1)
        totalHarga=int(harga+pajak)
    elif listFigure == "4":
        namaFigure= " Glitter & Glamours Figure Super Sailor Neptune - Pretty Guardian Sailor Moon Eternal The Movie (25cm) "
        harga=int(320000*jumlah)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    elif listFigure == "5":
        namaFigure= " PVC Figure 1/7 Caster / Altria Caster - 2nd Ascension "
        harga=int(3450000*jumlah)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    else:
        menu=input(" Maaf, Figure yang kamu pilih belum tersedia di toko kami. ")
 

    print(coverstrip)
    print(" Barang :",namaFigure)
    print(" Jumlah Pesanan :", jumlah)
    print(" Harga :", harga)
    print(" Pajak :", pajak)
    print(coverstrip)
    print(" Total Pembayaran :", totalHarga)
    print(coverstrip)
    print("Terima kasih telah berbelanja di Figure shop kami.")
    print(coverstrip)

coverstrip = '-'*55
print(coverstrip)
print("                 Violet Figure Shop                    ")
print(coverstrip)
print("Ketik 1 jika anda ingin login sebagai Admin")
print("Ketik 2 jika anda ingin login sebagai Pembeli")
print(coverstrip)
toko_login = int(input("Masukkan Pilihan: "))
if toko_login==1:
    login_admin()
    admin_toko()
if toko_login==2:
    login_pembeli()
    pembeli_toko()
