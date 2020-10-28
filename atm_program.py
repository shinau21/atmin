import datetime
import locale
import os
import os.path
from os import path
from time import sleep
from random import randint
from os import system,name
from customer import Customer

def checklogin(r,p):
    akun = Customer(r,p)
    if (r == akun.checkCard() and p == akun.checkPin()):
        return True
    else:
        return False

def banner():
    print("================================================")
    print("            BANK  PELAJAR  INDONESIA            ")
    print("================================================")
    print("Copyright : RAFLI SETIAWAN (@shinau_store)")
    print("")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    
locale.setlocale(locale.LC_ALL, '')
status = False
while True:
    count = 0
    while (status == False and count == 0):
        clear()
        banner()
        card = int(input("Masukan Nomor Kartu Anda : "))
        pin = int(input("Masukan PIN Anda : "))
        
        cl = checklogin(card,pin)
        if (cl != False):
            status = True
        else:
            count += 1


    while (status == False and count > 0 ):
        clear()
        banner()
        print("PIN yang anda masukan salah, silahkan coba lagi")
        pin = int(input("Masukan Kembali PIN Anda : "))
        cl = checklogin(card,pin)
        if (cl != False):
            status = True
        else:
            count += 1

        if (count == 3):
            print("Error, Silahkan coba lagi")
            exit()

    while (status == True):
        atm = Customer(card)
        clear()
        banner()
        print("Nama : " + atm.checkName())
        print("")
        print("1. Cek Saldo")
        print("2. Tarik Saldo")
        print("3. Simpan Saldo")
        print("4. Ganti PIN")
        print("5. Info Pengguna")
        print("0. Logout")
        print("")
        pil = input("Masukan Inputan (0-5) :")
        if pil == '1':
            clear()
            banner()
            saldo_idr = atm.checkIDR()
            saldo_usd = atm.checkUSD()
            saldo_kwd = atm.checkKWD()
            print("Saldo IDR : Rp.", '{0:n}'.format(saldo_idr))
            print("Saldo USD : $", '{0:n}'.format(saldo_usd))
            print("Saldo KWD : K.D ", '{0:n}'.format(saldo_kwd))
            sleep(2)

        elif pil == '2':
            clear()
            banner()
            print("1. Tarik Saldo IDR")
            print("2. Tarik Saldo USD")
            print("3. Tarik Saldo KWD")
            print("")
            inp_tar = input("Masukan Inputan Anda : ")
            if inp_tar == '1':
                clear()
                banner()
                lmt_tidr = 50000
                print("Minimal Penarikan Saldo IDR = Rp.", '{0:n}'.format(lmt_tidr))
                inp_nom = int(input("Masukan Nominal IDR Yang Akan Ditarik : "))
                s_idr = atm.checkIDR() - inp_nom
                if (inp_nom >= lmt_tidr):
                    if (atm.checkIDR() >= inp_nom and s_idr >= lmt_tidr):
                        atm.witdrawIDR(inp_nom)
                        print("Saldo IDR Yang Anda Tarik : Rp.", str(inp_nom))
                        print("Sisa Saldo IDR Anda : Rp.", '{0:n}'.format(atm.checkIDR()))
                        sleep(2)
                    elif (s_idr < lmt_tidr):
                        print("Saldo Tersisa Harus Lebih Dari Rp." + str(lmt_tidr-1))
                        sleep(2)
                    else:
                        print("Saldo IDR Tidak Cukup Untuk Melakukan Penarikan")
                        sleep(2)
                else:
                    lmt = 49999
                    print("Nominal Yang Anda Masukan Terlalu Sedikit")
                    print("Silahkan Coba Lagi")
                    print("Pastikan Nominal Yang Anda Masukan Harus Lebih Dari Rp.", '{0:n}'.format(lmt))
                    sleep(2)
            
            if inp_tar == '2':
                clear()
                banner()
                lmt_tusd = 10.00
                print("Minimal Penarikan Saldo USD = $", '{0:n}'.format(lmt_tusd))
                inp_nom = float(input("Masukan Nominal USD Yang Akan Ditarik : "))
                s_usd = atm.checkUSD() - inp_nom
                if (inp_nom >= lmt_tusd):
                    if (atm.checkUSD() >= inp_nom and s_usd >= lmt_tusd):
                        atm.witdrawUSD(inp_nom)
                        print("Saldo USD Yang Anda Tarik : Rp.", str(inp_nom))
                        print("Sisa Saldo USD Anda : Rp.", '{0:n}'.format(atm.checkUSD()))
                        sleep(2)
                    elif (s_usd < lmt_tusd):
                        print("Saldo Tersisa Harus Lebih Dari $" + str(lmt_tusd-0.01))
                        sleep(2)
                    else:
                        print("Saldo USD Tidak Cukup Untuk Melakukan Penarikan")
                        sleep(2)
                else:
                    lmt = 9.99
                    print("Nominal Yang Anda Masukan Terlalu Sedikit")
                    print("Silahkan Coba Lagi")
                    print("Pastikan Nominal Yang Anda Masukan Harus Lebih Dari", str(lmt))
                    sleep(2)

            if inp_tar == '3':
                clear()
                banner()
                lmt_tkwd = 5.00
                print("Minimal Penarikan Saldo KWD = " + str(lmt_tkwd))
                inp_nom = float(input("Masukan Nominal KWD Yang Akan Ditarik : "))
                s_kwd = atm.checkKWD() - inp_nom
                if (inp_nom >= lmt_tkwd):
                    if (atm.checkKWD() >= inp_nom and s_kwd >= 5.00):
                        atm.witdrawKWD(inp_nom)
                    elif (s_kwd < lmt_tkwd):
                        print("Saldo Tersisa Harus Lebih Dari Rp." + str(lmt_tkwd-0.01))
                        sleep(2)
                    else:
                        print("Saldo KWD Tidak Cukup Untuk Melakukan Penarikan")
                        sleep(2)
                else:
                    lmt = 5.00
                    print("Nominal Yang Anda Masukan Terlalu Sedikit")
                    print("Silahkan Coba Lagi")
                    print("Pastikan Nominal Yang Anda Masukan Harus Lebih Dari K.D.", str(lmt))
                    sleep(2)

        elif pil == '3':
            clear()
            banner()
            print("1. Simpan Saldo IDR")
            print("2. Simpan Saldo USD")
            print("3. Simpan Saldo KWD")
            print("")
            inp_sim = input("Masukan Inputan Anda : ")
            if inp_sim == '1':
                clear()
                banner()
                inp_nom = int(input("Masukan Nominal IDR Yang Akan Disimpan : "))
                atm.depositIDR(inp_nom)
                print("Rp." + '{0:n}'.format(inp_nom) + " Berhasil Ditambahkan Ke Saldo IDR")
                sleep(2)
            
            if inp_sim == '2':
                clear()
                banner()
                inp_nom = float(input("Masukan Nominal USD Yang Akan Disimpan : "))
                atm.depositUSD(inp_nom)
                print("$" + '{0:n}'.format(inp_nom) + " Berhasil Ditambahkan Ke Saldo USD")
                sleep(2)

            if inp_sim == '3':
                clear()
                banner()
                inp_nom = int(input("Masukan Nominal KWD Yang Akan Disimpan : "))
                atm.depositKWD(inp_nom)
                print("K.D." + '{0:n}'.format(inp_nom) + " Berhasil Ditambahkan Ke Saldo KWD")
                sleep(2)

        elif pil == '4':
            clear()
            banner()
            p_ver = int(input("Masukan PIN Lama Anda : "))
            if (atm.checkPin() == p_ver):
                clear()
                banner()
                gp = int(input("Masukan PIN Baru Anda : "))
                if (p_ver != gp):
                    atm.changePin(gp)
                    clear()
                    banner()
                    print("PIN baru anda : " + str(gp))
                    sleep(2)
                else:
                    print("Anda tidak bisa membuat PIN baru dengan PIN lama")
                    sleep(1)
            else:
                print("PIN Lama Yang Anda Masukan Salah")
                sleep(1)

        elif pil == '5':
            clear()
            banner()
            print("===============================")
            print("       Informasi Nasabah       ")
            print("================================")
            print("Nama     : " + atm.checkName())
            print("Gender   : " + atm.checkGender())
            print("Member   : " + atm.checkJenis())
            print("Alamat   : " + atm.checkAlamat())
            print("Nama Ibu : " + atm.checkIbu())
            sleep(2)

        elif pil == '0':
            clear()
            banner()
            saldo_idr = atm.checkIDR()
            saldo_usd = atm.checkUSD()
            saldo_kwd = atm.checkKWD()
            rec = randint(100000,1000000)
            date = str(datetime.datetime.now())
            print("Record : " + str(rec))
            print("Waktu : " + date)
            print("Saldo IDR : Rp.", '{0:n}'.format(saldo_idr))
            print("Saldo USD : $", '{0:n}'.format(saldo_usd))
            print("Saldo KWD : K.D ", '{0:n}'.format(saldo_kwd))
            
            if(path.exists("nasabah\\" + str(atm.checkCard()) + ".txt")):
                file = open("nasabah\\" + str(atm.checkCard()) + ".txt", "a")
                file.write("\n")
                file.write("Record    : " + str(rec) + "\n")
                file.write("Waktu     : " + date + "\n")
                file.write("Rekening  : " + str(atm.checkCard()) + "\n")
                file.write("Saldo IDR : Rp." + '{0:n}'.format(saldo_idr) + "\n")
                file.write("Saldo USD : $" + '{0:n}'.format(saldo_usd) + "\n")
                file.write("Saldo KWD : K.D " + '{0:n}'.format(saldo_kwd) + "\n")
                file.close()
            else:
                file = open("nasabah\\" + str(atm.checkCard()) + ".txt", "w+")
                file.write("===================================================\n")
                file.write("                  Riwayat Nasabah                  \n")
                file.write("===================================================\n")
                file.write("No Rek    : " + str(atm.checkCard()) + "\n")
                file.write("Nama      : " + str(atm.checkName()) + "\n")
                file.write("\n")
                file.write("\n")
                file.write("Record    : " + str(rec) + "\n")
                file.write("Waktu     : " + date + "\n")
                file.write("Rekening  : " + str(atm.checkCard()) + "\n")
                file.write("Saldo IDR : Rp." + '{0:n}'.format(saldo_idr) + "\n")
                file.write("Saldo USD : $" + '{0:n}'.format(saldo_usd) + "\n")
                file.write("Saldo KWD : K.D " + '{0:n}'.format(saldo_kwd) + "\n")
                file.close()

            status = False
        else:
            clear()
            banner()
            print("Maaf input yang anda masukan tidak ada dalam daftar menu")
            print("Silahkan coba lagi")
            sleep(1)