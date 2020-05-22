import requests,time,sys,random

from colorama import *
from colorama import Fore, Back, init
from random import choice

init()

la7mar = '\033[91m'
la5dhar = '\033[92m'
ramadi = '\033[90m'
blid = '\033[1m'
star = '\033[4m'
bigas = '\033[07m'
bigbbs = '\033[27m'
hell = '\033[05m'
saker = '\033[25m'
labyadh = '\033[00m'
cyan = '\033[0;96m'


def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
 
 ________  ___ _____   _____                _           
/  ___|  \/  |/  ___| /  ___|              | |          
\ `--.| .  . |\ `--.  \ `--.  ___ _ __   __| | ___ _ __ 
 `--. \ |\/| | `--. \  `--. \/ _ \ '_ \ / _` |/ _ \ '__|
/\__/ / |  | |/\__/ / /\__/ /  __/ | | | (_| |  __/ |   
\____/\_|  |_/\____/  \____/ \___|_| |_|\__,_|\___|_|   
      
 
 SMS Sender V1.0    |   Priv8 Bot    | |  Code by YoungHood                           
                 Greetz to : Amir-tn &&  Escanor 0xtn         
                      
 [+] My ICQ: 752920323


 [+] 1. Run SMS Sender v1.0 
 [+] 2. About me [ for any help ! ]

+-------- With Great Power Comes Great Responsibilities! --------+

			                  """
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )


logo()

choice=input(' [+] Select : ')
if choice=='1':
 def main():
  x = """\n\033[32mFrom Name = Sender name (ex : Facebook)
List of N° = put your number in a file .txt
Subject = The message

N.B*: Numbers in .txt file should be like : +countrycode-number
E.X: +380-979805709\n"""
  print (x)
  sender=str(input('\n\033[0m[+] From Name >  \033[32m'))
  inputs=open(input('\n\033[0m[+] List of N° (.txt) > \033[32m'),'r').read().splitlines()
  msg=str(input('\n\033[0m[+] Subject > \033[32m'))
  print('\n\033[0m[+] ToTal numbers : '+str(len(inputs)))
  time.sleep(1)
  print("\nlet's Start")
  for i in inputs:
   code=i.split('-')[0]
   num=i.split('-')[1]
   if '+' in str(code):
    code=code.replace('+','')
   bitch=requests.get('http://api.msg91.com/api/sendhttp.php?sender='+sender+'&route=4&mobiles='+num+'&authkey=201074AfPVnOOJCq5a9d4f8e&country='+code+'&message='+msg)
   print('\n[+] Sending To '+str(i)+'\n Statut :\033[92m Succes' )
 try:
  main()
 except FileNotFoundError:
   print('\nFile Not Found :|\n')
   sys.exit(0)
elif choice =='2':
 xx = """\n\033[32mName: YoungHood 
Age : n/a
Current Location : France
Job : Seller (I sell Office365 Sender inbox & Leads & Fud Pages, shells, cpanels, smtps, bots ...)

ICQ : 752920323 
Telegram : @UltraSender
E-mail : youngxhood@gmail.com\n"""
 print(xx)
