from curses.ascii import isalnum
import getpass
import string
from turtle import clear

stokMobil = [
    {"plat" : "B1234AB",
        "model" : "Yaris",
        "manufaktur" : "Toyota",
        "tahun" : "2015",
        "sewa"  : 450000,
        "transmisi" : "AT",
        "status" : {
            "tersedia"  : True,
            "nama"   : "",
            "nik"       : "",
            "durasi" :  0
        }
    },

    {"plat" :"B2508MHO", 
        "model" : "Avanza",
        "manufaktur" : "Toyota",
        "tahun" : "2013",
        "sewa"  : 350000,
        "transmisi" : "MT",
        "status" : {
            "tersedia"  : True,
            "nama"   : "",
            "nik"       : "",
            "durasi" :  0
        }
    },

    {"plat" :"B3048YOW",
        "model" : "Avanza",
        "manufaktur" : "Toyota",
        "tahun" : "2013",
        "sewa"  : 400000,
        "transmisi" : "AT",
        "status" : {
            "tersedia"  : True,
            "nama"   : "",
            "nik"       : "",
            "durasi" :  0
        }
    },

    {"plat" :"B6781PLA",
        "model" : "Xenia",
        "manufaktur" : "Daihatsu",
        "tahun" : "2013",
        "sewa"  : 350000,
        "transmisi" : "MT",
        "status" : {
            "tersedia"  : True,
            "nama"   : "",
            "nik"       : "",
            "durasi" :  0
        }
    },

    {"plat" :"B8982FKL",
        "model" : "Yaris",
        "manufaktur" : "Toyota",
        "tahun" : "2015",
        "sewa"  : 450000,
        "transmisi" : "AT",
        "status" : {
            "tersedia"  : False,
            "nama"   : "Petra",
            "nik"       : "78123",
            "durasi" :  23
        }
    },
]

cart = {
    "index" : None,
    "nama"   : "",
    "duration"  : 0,
    "nik"   : "",
    "saldo" : 0
}

def cekKetersediaan(checker):         # Output: True/False/None
    if isinstance(checker, int) == True:          # Input is index
        if (checker in range(0, len(stokMobil))) == True:
            return stokMobil[checker]["status"]["tersedia"]
        else:
            return None
    elif checker.isalnum() == True:   # Input is license plate               
        for i in range(len(stokMobil)):         
            if checker in stokMobil[i]["plat"]:   
                return stokMobil[i]["status"]["tersedia"]
            else:
                continue      
    else:
        return None 

def inputNama():
    while True:
        try:
            name = str((input("Masukkan nama: ")))
        except:
            print("Input invalid! Cek kembali penulisan nama.")
        else:
            return name

def inputNIK():
    while True:
            NIK = (input("Masukkan 5 digit NIK: "))
            if len(NIK) == 5:
                return NIK
            else:
                print("Input invalid! NIK tidak boleh melebihi 5 digit.")

def inputDurasi():
    while True:
        duration = abs(int(input("Silakan input durasi penyewaan (hari): ")))
        if duration > 0 and duration < 121:
            return duration
        else:
            print("Maaf, pilihan anda invalid atau melampaui batas penyewaan mobil (4 bulan)!")
            print("Silakan coba lagi!")

def inputSaldo():
    global cart
    print(f'Saldo anda adalah: {cart["saldo"]}')
    print("Masukkan saldo anda.")
    print(zero_return)

    cart["saldo"] += abs(int(input(">> ")))
    

def listMobil(dec=0):
    print ("{:<3} {:<10} {:<10} {:<11} {:<8} {:<12} {:<10} {:<10}".format('No', 'Plat',
    'Model','Manufaktur','Tahun', 'Sewa/Hari', 'Transmisi', 'Tersedia'))
    print(straightLine)
    if dec==0:                  # List semua mobil
        for i in range(len(stokMobil)):
            print ("{:<3} {:<10} {:<10} {:<11} {:<8} Rp. {:<12} {:<10} {:<6}".format(i+1,
                stokMobil[i]['plat'], stokMobil[i]['model'], stokMobil[i]['manufaktur'],
                stokMobil[i]['tahun'], stokMobil[i]['sewa'], stokMobil[i]['transmisi'], 
                'Ya' if stokMobil[i]['status']["tersedia"] else 'Tidak'))
    elif dec in range(1, len(stokMobil)+1):                         # Tunjukkan mobil tertentu
        dec -= 1
        print ("{:<3} {:<10} {:<10} {:<11} {:<8} Rp. {:<12} {:<10} {:<6}".format(dec+1,
            stokMobil[dec]['plat'], stokMobil[dec]['model'], stokMobil[dec]['manufaktur'], 
            stokMobil[dec]['tahun'], stokMobil[dec]['sewa'], stokMobil[dec]['transmisi'], 
            'Ya' if stokMobil[dec]['status']["tersedia"] else 'Tidak'))
    else:
        print("***Maaf, pilihan anda tidak terdapat dalam stok kami. Silakan coba lagi!***")
    print(straightLine + "\n")

def listPenyewa(dec=0):
    print ("{:<3} {:<10} {:<50} {:<10} {:<7}".format('No', 'Plat',
        'Nama','NIK','Durasi'))
    print(straightLine)
    if dec==0:                          # List semua penyewa
        for i in range(len(stokMobil)):
            if stokMobil[i]['status']["tersedia"] == False:
                print ("{:<3} {:<10} {:<50} {:<10} {:<7}".format(i+1, stokMobil[i]['plat'],
                stokMobil[i]['status']["nama"],stokMobil[i]['status']["nik"],
                stokMobil[i]['status']["durasi"]))
    elif dec in range(1, len(stokMobil)+1):         # List a specific renter
        # if stokMobil[dec]["status"]["tersedia"] == True:
        if cekKetersediaan(dec):
            print("Maaf, mobil ini belum dirental, sehingga tidak ada data penyewa yang terkait dengan mobil ini.")
        else:
            dec -= 1
            print ("{:<3} {:<10} {:<50} {:<10} {:<7}".format(dec+1, stokMobil[dec]['plat'],
                stokMobil[dec]['status']["nama"],stokMobil[dec]['status']["nik"],
                stokMobil[dec]['status']["durasi"]))
    else:
        print("***Maaf, pilihan anda tidak terdapat dalam stok kami. Silakan coba lagi!***")
    print(straightLine + "\n")

def carSelect():
    global cart
    listMobil()
    print("Masukkan angka (\"No\" sesuai tabel) mobil keinginan anda.")
    print(zero_return)
    decision = int(input(">> "))
    if decision == 0:
        return 0
    elif decision > 0 and decision <= len(stokMobil):
        cart["index"] = decision 
        return decision
    else:
        print("Pilihan tidak tersedia!")
        return decision
        
def checkout():
    global cart
    index = cart["index"]-1
    total = cart["durasi"] * stokMobil[index]["sewa"]
    print(f'Total: {stokMobil[index]["sewa"]} * {cart["durasi"]} Hari = Rp. {total}')
    while cart["saldo"] < total:
        print("{}Total yang harus anda bayar adalah: Rp. {}".format(
            'Saldo anda kurang. ' if cart["saldo"] < total else '', total))
        inputSaldo()
        if cart["saldo"] == 0:
            return 0
        elif cart["saldo"] >= total:
            cart["saldo"] -= total
            print(f'Kembalian anda adalah: Rp. {cart["saldo"]}\n' if cart["saldo"] > 0 else "")
            break
        else:
            continue
    return cart

def ubahKeterangan(inputMobil=0,index=0):
    global tambahanTemp
    if inputMobil != 0:
        tambahanTemp = inputMobil

    while True:
        print ("\n{:<3} {:<10} {:<10} {:<11} {:<8} {:<12} {:<10} {:<6}".format(
            'No', 'Plat', 'Model','Manufaktur','Tahun', 'Sewa/Hari', 
            'Transmisi', 'Tersedia'))
        print(straightLine)
        print ("{:<3} {:<10} {:<10} {:<11} {:<8} Rp. {:<12} {:<10} {:<6}".format(
            int(len(stokMobil)+1) if inputMobil == 0 else index, 
            tambahanTemp['plat'], tambahanTemp['model'], tambahanTemp['manufaktur'], 
            tambahanTemp['tahun'], tambahanTemp['sewa'], tambahanTemp['transmisi'], 
            'Ya' if tambahanTemp['status']["tersedia"] else 'Tidak'))
        print(straightLine)

        print('''\n1. Ubah plat
2. Ubah Model Mobil
3. Ubah Manufaktur Mobil
4. Ubah Tahun Produksi
5. Ubah Harga Sewa/Hari
6. Ubah Transmisi
7. Ubah ketersediaan
8. Selesai dan tambahkan

Silakan pilih data yang ingin anda ganti.''')
        print(zero_return)
        decision = abs(int(input(">> ")))
        if decision == 1:
            tambahanTemp['plat'] = input("Masukkan plat nomor (harus lebih dari 3 digit): ")
        elif decision == 2:
            tambahanTemp['model'] = input("Masukkan nama model mobil: ")
        elif decision == 3:
            tambahanTemp['manufaktur'] = input("Masukkan nama manufaktur mobil: ")
        elif decision == 4:
            tambahanTemp['tahun'] = input("Masukkan tahun produksi mobil: ")
        elif decision == 5:
            tambahanTemp['sewa'] = int(input("Masukkan harga sewa per hari mobil: "))
        elif decision == 6:
            while True:
                print("Apakah transmisi mobil ini:")
                print("1. Otomatis (AT)")
                print("2. Manual (MT)")
                decision = abs(int(input(">> ")))
                if decision is 1 or 2:
                    tambahanTemp["transmisi"] = "AT" if decision == 1 else "MT"
                    break
                else:
                    print("Input salah! Silakan coba lagi")            
        elif decision == 7:
            while True:
                print("Apakah mobil ini tersedia?")
                print("1. Iya, mobil ini tersedia")
                print("2. Tidak, mobil ini sedang dirental (lanjut ke memasukkan data penyewa)")
                decision = abs(int(input(">> ")))
                if decision == 1:
                    tambahanTemp["status"]["tersedia"] = True
                    tambahanTemp["status"]["nama"] = ""
                    tambahanTemp["status"]["nik"] = ""
                    tambahanTemp["status"]["durasi"] = 0
                    break
                elif decision == 2:
                    tambahanTemp["status"]["tersedia"] = False
                    tambahanTemp["status"]["durasi"] = inputDurasi()
                    tambahanTemp["status"]["nama"] = inputNama()
                    tambahanTemp["status"]["nik"] = inputNIK()
                    print ("{:<3} {:<10} {:<50} {:<10} {:<7}".format('No', 'Plat',
        'Nama','NIK','Durasi'))
                    print(straightLine)
                    print ("{:<3} {:<10} {:<50} {:<10} {:<7}".format(
                        int(len(stokMobil)+1) if inputMobil == 0 else index,
                        tambahanTemp['plat'], tambahanTemp['status']["nama"],
                        tambahanTemp['status']["nik"], tambahanTemp['status']["durasi"]))
                    print(straightLine)
                    print("Data penyewa berhasil ditambahkan!")
                    break
                else:
                    print("Input salah! Silakan coba lagi")
        elif decision == 8:
            if "" in tambahanTemp.values():
                print("Ada keterangan yang kosong. Mohon cek kembali input anda!")    
            else:
                return tambahanTemp
                
        elif decision == 0:
            return 0
        else:
            print("\nPilihan tidak valid! Silahkan cek kembali pilihan anda.")

def updateStok(values, infoType, specificIndex=None):             # Change value with a key
    if specificIndex == None:
        if infoType == 1:                                   # Update through renting a car, change status to 'False' (unavailable)
            index = values["index"]-1                   # Minus 1 to fit the display in list
            stokMobil[index]["status"]["tersedia"] = False
            stokMobil[index]["status"]["nama"] = values["nama"]
            stokMobil[index]["status"]["nik"] = values["nik"]
            stokMobil[index]["status"]["durasi"] = values["durasi"]
        elif infoType == 2:                                            # Update through returning a car, change status to 'True' (available)
            stokMobil[values]["status"]["tersedia"] = True
            stokMobil[values]["status"]["nama"] = ""
            stokMobil[values]["status"]["nik"] = ""
            stokMobil[values]["status"]["durasi"] = 0
        elif infoType == 3:
            stokMobil.append(values)
        else:
            pass
    else:                                                 # Update a single value within the stok (used in pengaturan)
        stokMobil[specificIndex] = values

def cleartambahanTemp():
    global tambahanTemp

    tambahanTemp = {
    "plat" : "",
    "model" : "",
    "manufaktur" : "",
    "tahun" : "",
    "sewa"  : "",
    "transmisi" : "",
    "status" : {
        "tersedia"  : True,
        "nama"   : "",
        "nik"       : "",
        "durasi" :  0
    }
}

straightLine = "-"*83

doubleStraightLine = "="*83

tambahanTemp = {
    "plat" : "",
    "model" : "",
    "manufaktur" : "",
    "tahun" : "",
    "sewa"  : "",
    "transmisi" : "",
    "status" : {
        "tersedia"  : True,
        "nama"   : "",
        "nik"       : "",
        "durasi" :  0
    }
}

zero_return = ('''-----------------------------------------------------------------------------------
0. Kembali''')

alRentLogo = ('''
                  d8888 888        8888888b.                   888    
                 d88888 888        888   Y88b                  888    
                d88P888 888        888    888                  888    
               d88P 888 888        888   d88P .d88b.  88888b.  888888 
              d88P  888 888        8888888P" d8P  Y8b 888 "88b 888    
             d88P   888 888 888888 888 T88b  88888888 888  888 888    
            d8888888888 888        888  T88b Y8b.     888  888 Y88b.  
           d88P     888 888        888   T88b "Y8888  888  888  "Y888 
                                                      "Al-Rent a Car!"''')


decision = 1


# Main Starts Here
print(alRentLogo)

while True:
    print("\nSelamat datang di Al-Rent! Sahabat perjalanan Anda.")
    print(doubleStraightLine)
    print(f'''1. Tampilkan List Mobil 
2. Sewa Mobil
3. Kembalikan Mobil
4. Pengaturan
0. Keluar
''')

    decision = abs(int(input(">> ")))

    if decision == 1:
            print("\nI. Tampilkan List Mobil")
            print(doubleStraightLine)
            listMobil()

    elif decision == 2:
        print("\nII. Sewa Mobil")
        print(doubleStraightLine)
        while decision !=0:
            decision = carSelect()
            if decision == 0:
                break
            elif decision > 0 and decision <= len(stokMobil):
                tersedia = cekKetersediaan(decision-1)
                # decision-1 because the table displays the list from 1, 
                # whereas stokMobil index starts from 0

                if tersedia == True:
                    print("Pilihan Anda adalah:")
                    listMobil(decision)
                    print('''Apakah anda yakin ingin memilih mobil ini?
1. Iya
2. Pilih yang lain''')
                    decision = int(input(">> "))
                    
                    if decision == 1:
                        cart["durasi"] = inputDurasi()
                        cart["nama"] = inputNama()
                        cart["nik"] = inputNIK()
                        while True:
                            print("\n" + doubleStraightLine)
                            print("Pastikan data Anda sudah tepat sebelum melanjutkan ke proses pembayaran.\n")
                            print("1. Pilihan Kendaraan:")
                            listMobil(cart["index"])
                            print("2. Durasi Penyewaan: ", cart["durasi"])
                            print("3. Nama Penyewa: ", cart["nama"])
                            print("4. NIK Penyewa: ", cart["nik"])
                            print("5. Lanjut dan bayar")

                            print("\n" + zero_return)

                            decision = abs(int(input(">> ")))
                            if decision == 1:
                                decision = carSelect()
                                if decision == 0:
                                    continue
                            elif decision == 2:
                                cart["durasi"] = inputDurasi()
                            elif decision == 3:
                                cart["nama"] = inputNama()
                            elif decision == 4:
                                cart["nik"] = inputNIK()
                            elif decision == 5:
                                exitCode = checkout()
                                if exitCode == 0:
                                    # cart.clear()
                                    break
                                else:
                                    updateStok(exitCode,1)      # the exitCode contains data of the renter, updateStok(-,1) means stok is updated by renting
                                    decision = 0
                                    print("Terima kasih! Hati-hati di jalan!")
                                    # cart.clear()
                                    break
                            elif decision == 0:
                                break
                            else:
                                print("Input invalid. Silakan coba lagi!")
                    else:
                        continue
                else:
                    print("Maaf, pilihan Anda tidak tersedia! Silakan coba lagi.")
                    continue
            else:
                print("Pilihan anda tidak valid! Cek kembali pilihan anda.")
                continue


    elif decision == 3:
        print("\nIII. Kembalikan Mobil")
        print(doubleStraightLine)
        while True:
            foundIndex = None 
            print("\nMasukkan plat nomor mobil sewaan anda.")
            print(zero_return)
            decision = input(">> ")
            if decision == "0":             
                # because the input has to be string, the checker has to also to be string
                decision = 0
                break
            elif len(decision) > 3 and decision.isalnum() == True:
                # Find the index then assign the value into foundIndex
                # If not found, back to plate number input
                for i in range(len(stokMobil)):
                    if stokMobil[i]["plat"] == decision:
                        foundIndex = i
                        break
                # print(f"foundIndex: {foundIndex}")
                # tersediaKah = cekKetersediaan(foundIndex)
                if foundIndex == None:
                    print("\nPlat nomor tidak ditemukan! Silakan coba lagi.")
                elif cekKetersediaan(foundIndex) == True:
                        print("Mobil ini belum dirental, sehingga tidak bisa dikembalikan.")
                        print("Silakan coba lagi!")
                        decision = 3
                else:
                    print('\nBerikut adalah pilihan anda:')
                    listMobil(foundIndex+1)
                    print('\nDan berikut adalah data penyewa mobil ini:')
                    listPenyewa(foundIndex+1)
                    print('''Apakah anda yakin ingin mengembalikan mobil ini?
1. Ya
0. Tidak (kembali ke memasukkan plat nomor)
                    ''')
                    decision = int(input(">> "))
                    if decision == 1:
                        updateStok(foundIndex,2)
                        listMobil(foundIndex+1)
                        print("Mobil berhasil dikembalikan!")
                        break
                    else:
                        listMobil(foundIndex+1)
                        print("Mobil belum dikembalikan.")           
            else:
                print("\nPilihan tidak valid. Pastikan anda tidak menggunakan spasi saat memasukkan plat nomor.")
    elif decision == 4:
        print("\nIV. Pengaturan")
        print(doubleStraightLine)
        print("Menu ini diperuntukkan kepada staf Al-Rental untuk keperluan inventaris.")
        print("Pelanggan dilarang mengakses menu ini!")
        
        while True:
            print(f'''\n1. Tambah Mobil
2. Hapus Mobil
3. Ubah Keterangan Mobil
''')
            print(zero_return)
            decision = abs(int(input(">> ")))
            if decision == 1:
                print("\nAnda akan menambahkan kendaraan berikut ke stok mobil.")
                decision = ubahKeterangan()
                if decision != 0:
                    updateStok(tambahanTemp,3)
                    listMobil()
                    print("Perubahan berhasil!")
                    cleartambahanTemp()
                else:
                    print("Tidak ada data yang berubah.")
                    cleartambahanTemp()
                    continue
            elif decision == 2:
                while True:
                    print("\nBerikut adalah keseluruhan stok mobil.")
                    print("Silakan pilih mobil sesuai yang anda ingin hapus.")
                    decision = carSelect()
                    if decision == 0:
                        break
                    elif decision > 0 and decision <= len(stokMobil):
                        selection = decision
                        while True:
                            print("Berikut adalah pilihan Anda:")
                            listMobil(selection)
                            print("Apakah anda yakin ingin menghapus mobil ini dari stok?")
                            print(f'''1. Ya, hapus mobil
0. Kembali (mobil akan tetap berada di stok)
                            ''')
                            decision = abs(int(input(">> ")))
                            if decision == 0:
                                print("Tidak ada data yang berubah.")
                                break
                            elif decision == 1:
                                stokMobil.pop(selection-1)
                                listMobil()
                                print("Mobil berhasil dihapus dari stok!")
                                break
                            else:
                                print("Pilihan anda tidak valid. Silakan cek input Anda!")
                    else:
                        print("Pilihan anda tidak valid atau tidak ada dalam stok. Silakan cek kembali input Anda!")

            elif decision == 3:
                print("\nBerikut adalah keseluruhan stok mobil.")
                print("Silakan pilih keterangan mobil yang ingin anda hapus.")
                listMobil()
                print(zero_return)
                decision = int(input(">> "))
                if decision == 0:
                    continue
                else: 
                    keteranganBaru = ubahKeterangan(stokMobil[decision-1],decision)
                    if keteranganBaru == 0:
                        print("Tidak ada data yang berubah.")
                        cleartambahanTemp()
                        continue
                    else:
                        updateStok(keteranganBaru, None, selection)
                        listMobil()
                        cleartambahanTemp()
            elif decision == 0:
                break
            else:
                print("\nPilihan tidak valid! Silahkan cek kembali pilihan anda.")

    elif decision == 0:
        print("Terminating program...")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi!")