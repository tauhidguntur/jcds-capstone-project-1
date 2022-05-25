from curses.ascii import isalnum
import getpass

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
            "nik"       : 0,
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
            "penyewa"   : "",
            "nik"       : 0,
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
            "nik"       : 0,
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
            "nik"       : 0,
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
            "nik"       : 0,
            "durasi" :  0
        }
    },
]

def cekKetersediaan(checker):         # Output: True/False/None
    if type(checker) == int:          # Input is index
        if (checker in range(1, len(stokMobil)+1)) == True:
            return stokMobil[checker]["status"]["tersedia"]
        else:
            return None
    elif checker.isalnum() == True:   # Input is license plate               
        for i in range(len(stokMobil)):         
            if checker in stokMobil[i]["plat"]:   
                return stokMobil[i]["status"]["tersedia"]
                
            else:
                break      
    else:
        return None 

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
                stokMobil[i]['plat'], stokMobil[i]['model'], stokMobil[i]['manufaktur'],
                stokMobil[i]['tahun'], stokMobil[i]['sewa'], stokMobil[i]['transmisi'], 
                'Ya' if stokMobil[i]['status']["tersedia"] else 'Tidak'))
    elif dec in range(1, len(stokMobil)+1):
        dec -= 1
        print ("|{:<3} {:<10} {:<10} {:<11} {:<8} Rp. {:<12} {:<10} {:<6}|".format(dec+1,
            stokMobil[dec]['plat'], stokMobil[dec]['model'], stokMobil[dec]['manufaktur'], 
            stokMobil[dec]['tahun'], stokMobil[dec]['sewa'], stokMobil[dec]['transmisi'], 
            'Ya' if stokMobil[dec]['status']["tersedia"] else 'Tidak'))
    else:
        print("***Maaf, pilihan anda tidak terdapat dalam stok kami. Silakan coba lagi!***")
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

    decision = abs(int(input(">> ")))

    if decision == 1:
            print("\nI. Tampilkan List Mobil")
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
    
    elif decision == 0:
        print("Terminating program...")
        break
    else:
        print("Pilihan invalid. Silakan coba lagi!")