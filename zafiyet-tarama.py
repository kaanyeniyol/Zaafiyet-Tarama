# -*- coding: utf-8 -*-
from subprocess import *
import subprocess , os, sys

basla = str(raw_input("IP taramak istiyorsaniz   1:  \naginiza bagli ipler icin  2:   \nms17-010 taramasi icin    3:    \nZaafiyet taramasi icin    4:  \n ->> " ))
if basla=="1":
    ip = "192.168.100.166"
    #os.system("ping "+ip)
    #print dizin
    print("\n")
    ip_adres = str(raw_input(">>  Taranacak ip adresi veya araligini gir : "))
    os.chdir("C:/")
    #os.system("ls")
    print(">>  .XML ciktisi alinsin mi ? E/H "),
    cikti_onay = str(raw_input());
    print("\n NMAP BASLATILIYOR ---------------------------------- \n")

    if cikti_onay=="E":
        os.system("nmap -sS -sV -p- "+ip_adres + " -oX "+ip_adres +".xml")
        print("cikti"),
        os.system("pwd"),
        print("dizinine kayit edilmistir.")
    else:
        os.system("nmap -sS -sV -p- "+ip_adres)
elif basla=="2":
    print("\n")
    ip_adres = str(raw_input(">>   ip adresinizi giriniz /24  : "))
    print("\n")
    os.system("nmap -sn "+ip_adres)
elif basla=="3":
    print("\n")
    ip_adres = str(raw_input(">>   ip adresinizi giriniz  : "))
    print("\n")
    os.system("nmap -p445 --script smb-vuln-ms17-010 "+ip_adres)
elif basla=="4":
    print("\n")
    ip_adres = str(raw_input(">>   ip adresinizi giriniz  : "))
    print("\n")
    os.system("nmap --script vuln "+ip_adres)
else:
    print("Gecersiz giris")
    sys.exit()
