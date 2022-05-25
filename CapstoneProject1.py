from curses.ascii import isalnum
import getpass
<<<<<<< HEAD
=======
import string
>>>>>>> 67b65b3 (Branch 1 almost finished)

stokMobil = [
    {"plat" : "B1234AB",
        "model" : "Yaris",
        "manufaktur" : "Toyota",
        "tahun" : "2015",
        "sewa"  : 450000,
        "transmisi" : "AT",
        "status" : {
            "tersedia"  : True,
            "penyewa"   : "",
<<<<<<< HEAD
            "nik"       : 0,
=======
            "nik"       : "",
>>>>>>> 67b65b3 (Branch 1 almost finished)
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
<<<<<<< HEAD
            "tersedia"  : True,
            "penyewa"   : "",
            "nik"       : 0,
=======
            "tersedia"  : False,
            "penyewa"   : "",
            "nik"       : "",
>>>>>>> 67b65b3 (Branch 1 almost finished)
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
            "penyewa"   : "",
<<<<<<< HEAD
            "nik"       : 0,
=======
            "nik"       : "",
>>>>>>> 67b65b3 (Branch 1 almost finished)
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
            "penyewa"   : "",
<<<<<<< HEAD
            "nik"       : 0,
=======
            "nik"       : "",
>>>>>>> 67b65b3 (Branch 1 almost finished)
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
            "tersedia"  : True,
            "penyewa"   : "",
<<<<<<< HEAD
            "nik"       : 0,
=======
            "nik"       : "",
>>>>>>> 67b65b3 (Branch 1 almost finished)
            "durasi" :  0
        }
    },
]

<<<<<<< HEAD
def cekKetersediaan(checker):         # Output: True/False/None
    if type(checker) == int:          # Input is index
        if (checker in range(1, len(stokMobil)+1)) == True:
=======
cart = {
    "index" : None,
    "nama"   : "",
    "duration"  : 0,
    "nik"   : "",
    "saldo" : 0
}

def cekKetersediaan(checker):         # Output: True/False/None
    if isinstance(checker, int) == True:          # Input is index
        checker -= 1
        if (checker in range(0, len(stokMobil))) == True:
>>>>>>> 67b65b3 (Branch 1 almost finished)
            return stokMobil[checker]["status"]["tersedia"]
        else:
            return None
    elif checker.isalnum() == True:   # Input is license plate               
        for i in range(len(stokMobil)):         
            if checker in stokMobil[i]["plat"]:   
                return stokMobil[i]["status"]["tersedia"]
<<<<<<< HEAD
                
=======
>>>>>>> 67b65b3 (Branch 1 almost finished)
            else:
                break      
    else:
        return None 

<<<<<<< HEAD
def inputDurasi():
    global cart
    global decision
    decision = None
    while True:
        print("Silakan input durasi penyewaan mobil ini (hari):")
        decision = abs(int(input(">> ")))
        if decision != 0 and decision < 121:
            cart["durasi"] = decision
        elif decision != 0 and decision > 121:
            print("Maaf, pilihan anda invalid atau melampaui batas penyewaan mobil (4 bulan)!")
            print("Silakan coba lagi!")
        else:
            decision



zero_return = ('''
-----------------------------------------------------------
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
-------------------------------------------"Al-Rent a Car!"''')

cart = {
    "nama" : "",
    "nik"  : "",
    "durasi" : 0,
    "pilihanMobil" : None
}
saldo = 0
decision = 1

def listMobil(dec=0):
    print('-' * 83)
    print ("|{:<3} {:<10} {:<10} {:<11} {:<8} {:<12} {:<10} {:<10}|".format('No', 'Plat',
    'Model','Manufaktur','Tahun', 'Sewa/Hari', 'Transmisi', 'Tersedia'))
    print('-' * 83)
    if dec==0:
        for i in range(len(stokMobil)):
            print ("|{:<3} {:<10} {:<10} {:<11} {:<8} Rp. {:<12} {:<10} {:<6}|".format(i+1,
=======
def inputNama():
    global cart
    while True:
        try:
            name = str((input("Masukkan nama anda: ")))
        except:
            print("Input invalid! Cek kembali penulisan nama anda.")
        else:
            cart["nama"] = name
            break

def inputNIK():
    global cart
    while True:
            NIK = (input("Masukkan 5 digit NIK anda: "))
            if len(NIK) == 5:
                cart["nik"] = NIK
                break
            else:
                print("Input invalid! NIK tidak boleh melebihi 5 digit.")

def inputDurasi():
    global cart
    while True:
        # print("Silakan input durasi penyewaan (hari):")
        duration = abs(int(input("Silakan input durasi penyewaan (hari): ")))
        if 0 < duration < 121:
            cart["durasi"] = duration
            break
        else:
            print("Maaf, pilihan anda invalid atau melampaui batas penyewaan mobil (4 bulan)!")
            print("Silakan coba lagi!")

def inputSaldo():
    global cart
    print(f'Saldo anda adalah: {cart["saldo"]}')
    print("Masukkan saldo sebanyak yang anda inginkan.")
    print(zero_return)

    cart["saldo"] += abs(int(input(">> ")))
    

def listMobil(dec=0):
    print ("{:<3} {:<10} {:<10} {:<11} {:<8} {:<12} {:<10} {:<10}".format('No', 'Plat',
    'Model','Manufaktur','Tahun', 'Sewa/Hari', 'Transmisi', 'Tersedia'))
    print(straightLine)
    if dec==0:
        for i in range(len(stokMobil)):
            print ("{:<3} {:<10} {:<10} {:<11} {:<8} Rp. {:<12} {:<10} {:<6}".format(i+1,
>>>>>>> 67b65b3 (Branch 1 almost finished)
                stokMobil[i]['plat'], stokMobil[i]['model'], stokMobil[i]['manufaktur'],
                stokMobil[i]['tahun'], stokMobil[i]['sewa'], stokMobil[i]['transmisi'], 
                'Ya' if stokMobil[i]['status']["tersedia"] else 'Tidak'))
    elif dec in range(1, len(stokMobil)+1):
        dec -= 1
<<<<<<< HEAD
        print ("|{:<3} {:<10} {:<10} {:<11} {:<8} Rp. {:<12} {:<10} {:<6}|".format(dec+1,
=======
        print ("{:<3} {:<10} {:<10} {:<11} {:<8} Rp. {:<12} {:<10} {:<6}".format(dec+1,
>>>>>>> 67b65b3 (Branch 1 almost finished)
            stokMobil[dec]['plat'], stokMobil[dec]['model'], stokMobil[dec]['manufaktur'], 
            stokMobil[dec]['tahun'], stokMobil[dec]['sewa'], stokMobil[dec]['transmisi'], 
            'Ya' if stokMobil[dec]['status']["tersedia"] else 'Tidak'))
    else:
        print("***Maaf, pilihan anda tidak terdapat dalam stok kami. Silakan coba lagi!***")
<<<<<<< HEAD
    print('-' * 83)
    


print(alRentLogo)

while True:
    print(f'''
-----------------------------------------------------------
Menu Utama. Silakan pilih:
===========================================================
1. Tampilkan List Mobil 
2. Sewa Mobil
3. Kembalikan Mobil
4. Pengaturan Saldo

Saldo Anda: Rp. {saldo}
-----------------------------------------------------------
0. Keluar
-----------------------------------------------------------
9. Menu Staf''')
=======
    print(straightLine + "\n")
    
def carSelect():
    global cart
    yakin = 0
    while yakin == 0:
        listMobil()
        print("Masukkan angka (\"No\") mobil rental keinginan anda sesuai dengan tabel di atas.")
        print(zero_return)
        decision = int(input(">> "))
        
        tersedia = cekKetersediaan(decision)

        if decision != 0 and tersedia == True:
            print("Pilihan Anda adalah:")
            listMobil(decision)
            print('''Apakah anda yakin untuk memilih mobil ini?
            1. Ya
            0. Tidak''')
            yakin = int(input(">> "))
        elif decision != 0 and tersedia == False:
            print("\nMaaf, pilihan anda tidak tersedia. Silakan coba lagi!\n")
        elif decision == 0:
            return 0
        else:
            print("Pilihan tidak valid. Silakan coba lagi!\n")
    
    cart["index"] = decision
    return decision
        
def checkout():
    global cart
    index = cart["index"]
    total = cart["durasi"] * stokMobil[index]["sewa"]
    print(f'Total: {stokMobil[index]["sewa"]} * {cart["durasi"]} Hari = Rp. {total}')
    while cart["saldo"] < total:
        print("{}Total yang harus anda bayar adalah: Rp. {}".format(
            'Saldo anda kurang. ' if cart["saldo"] < total else '', total))
        inputSaldo()
        if cart["saldo"] == 0:
            return 0
        elif cart["saldo"] > total:
            cart["saldo"] -= total
            print(f'Kembalian anda adalah: Rp. {cart["saldo"]}')
            printReceipt(cart)

        else:
            continue
    
    return cart


def updateStok(key,values):
    if key == 1:                        # Change status to unavailable (because of being rented)
        index = values["index"]
        stokMobil[index]["status"]["tersedia"] = False
        stokMobil[index]["status"]["penyewa"] = values["nama"]
        stokMobil[index]["status"]["nik"] = values["nik"]
        stokMobil[index]["status"]["durasi"] = values["durasi"]
    elif key == 0:                      # Change status to available (because of returned)
        pass
    elif isinstance(key,string) == True:
        pass
    else:
        print("Input Invalid!")

def printReceipt():
    pass

straightLine = "-"*83

doubleStraightLine = "="*83

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
>>>>>>> 67b65b3 (Branch 1 almost finished)

    decision = abs(int(input(">> ")))

    if decision == 1:
            print("\nI. Tampilkan List Mobil")
<<<<<<< HEAD
            print("=" * 59)
            listMobil()

    elif decision == 2:
        # menu2List = [inputDurasi(),inputDataPenyewa(),checkout()]
        print("II. Sewa Mobil")
        print("=" * 59)
        listMobil()
        print("Masukkan angka mobil rental keinginan anda sesuai dengan",
        "\ntabel di atas untuk memulai proses penyewaan.")
        print(zero_return)
        decision = abs(int(input(">> ")))
    
        while decision != 0 :
            if decision != 0 and cekKetersediaan(decision) == True:
                print("Pilihan anda adalah:")
                listMobil(decision)
                
                for i in range(len(menu2List)):
                    menu2List[i]()

                print(cart)
                decision = 0

            elif decision != 0 and cekKetersediaan(decision) == False:
                print("\nMaaf, pilihan anda tidak terdapat dalam stok kami. Silakan coba lagi!")
    
=======
            print(doubleStraightLine)
            listMobil()
            # sortList()

    elif decision == 2:
        print("\nII. Sewa Mobil")
        print(doubleStraightLine)
        while decision !=0:
            decision = carSelect()
            if decision == 0:
                break
            inputDurasi()
            inputNama()
            inputNIK()
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
                    inputDurasi()
                elif decision == 3:
                    inputNama()
                elif decision == 4:
                    inputNIK()
                elif decision == 5:
                    exitCode = checkout()
                    if exitCode == 0:
                        break
                    else:
                        updateStok(1,exitCode)      # the exitCode contains data of the renter, 1 means stok is updated through rent
                        decision = 0
                        break
                elif decision == 0:
                    break
                else:
                    print("Input invalid. Silakan coba lagi!")


            # elif decision != 0 and cekKetersediaan(decision) == False:
            #     print("\nMaaf, pilihan anda tidak terdapat dalam stok kami. Silakan coba lagi!")

    elif decision == 4:
        pass

>>>>>>> 67b65b3 (Branch 1 almost finished)
    elif decision == 0:
        print("Terminating program...")
        break
    else:
<<<<<<< HEAD
        print("Pilihan invalid. Silakan coba lagi!")
=======
        print("Pilihan tidak valid. Silakan coba lagi!")
>>>>>>> 67b65b3 (Branch 1 almost finished)
