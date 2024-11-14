

import hashlib
import argparse
import os
import time
from art import *
import random
from termcolor import colored
import os
from colorama import init
init()
from colorama import Fore, Back, Style
from time import sleep
import tqdm
import sys
import time
import platform
from os import system as cmd
import requests
import sys
from itertools import product
import re
from pathlib import Path
import threading

from platform import system as sy
 







        


def spinner_01(TEXT,stop):
    ERASE_LINE = '\x1b[2K' 
    print (TEXT+"........ \\",end="")
    syms = [Fore.LIGHTCYAN_EX+'\\', Fore.LIGHTCYAN_EX+'|',Fore.LIGHTCYAN_EX+ '/', Fore.LIGHTCYAN_EX+'-']
    bs = '\b'
    animation = '\\-|/'
    while True:
        for sym in syms:
            sys.stdout.write("\x1b[96m"+"\b%s" % sym)
            sys.stdout.flush()
            time.sleep(0.005)
        if stop():
            #sys.stdout.write(ERASE_LINE)
            #CURSOR_UP_ONE = '\x1b[1A' 
            #sys.stdout.write(CURSOR_UP_ONE)
            print(Style.RESET_ALL) 
            break
           


def hashcrackthretmode():
    clearTerminal()
    verbose = 'False'
    wordlistToUse = input('[#]Shell@Wordlist>> ')
    


    print(Fore.MAGENTA+'Wordlist> '+Style.RESET_ALL+wordlistToUse)
    hashToCrack = input('[#]Shell@Hash>> ')

    r = requests.get('https://hashes.com/en/api/identifier?hash={}'.format(hashToCrack))
    scode = 200

    if r.status_code==scode:
        algorithm = r.text.split('"')[-4]
        ty = r.text.split('"')[-2]
        #print("["+Fore,LIGHTGREEN_EX+"+"+Style.RESET_ALL+' Possible {} {}'.format(algorithm,ty))
    else:
        return False
    
    
        
        
    print(Fore.MAGENTA+'Hash> '+Style.RESET_ALL+hashToCrack)
    #algorithmToUse = input ('[#]Shell@Algorithm>> ')
    
    #print(Fore.MAGENTA+'algorithm> '+Style.RESET_ALL+algorithmToUse)
    print('[#] Verbose '+Fore.MAGENTA+'True'+Style.RESET_ALL+Fore.YELLOW+' False'+Style.RESET_ALL+Fore.LIGHTCYAN_EX+' Deepermode'+Style.RESET_ALL)
    verbose = input(str('[#]Shell@Verbose>> '))
    print(Fore.MAGENTA+'verbose> '+Style.RESET_ALL+verbose)
    pwdtries=0
    found = False
    CURSOR_UP_ONE = '\x1b[1A' 
    ERASE_LINE = '\x1b[2K' 
    stop_threads = False
    clearTerminal()
    t1 = threading.Thread(target = spinner_01, args =('Deeper Cracker Sytems Initializing',lambda : stop_threads, )) 
    t1.start() 
    sleep(5)
    stop_threads = True
    t1.join()            
    print(Fore.LIGHTCYAN_EX+"#"+Style.RESET_ALL+"====================================================================="+Fore.LIGHTCYAN_EX+"#"+Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX+"#"+Style.RESET_ALL+" ================== <"+Fore.LIGHTCYAN_EX+" Initializing Deeper Cracker"+Style.RESET_ALL+" > ================="+Fore.LIGHTCYAN_EX+"#"+Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX+"#"+Style.RESET_ALL+"====================================================================="+Fore.LIGHTCYAN_EX+"#"+Style.RESET_ALL)
      
    print('['+Fore.LIGHTGREEN_EX+'+'+Style.RESET_ALL+'] '+"{} Hash {}".format(ty,hashToCrack))
    wo = wordlistToUse.split('\\')[-1]
    print("["+Fore.LIGHTGREEN_EX+"+"+Style.RESET_ALL+"] "'wordlist {}'.format(wo))
    print("["+Fore.LIGHTGREEN_EX+'+'+Style.RESET_ALL+'] '+"Possible Hash algorithm {}".format(ty))
    starttime=time.time()
    try:
        with open(wordlistToUse, mode="r",encoding="utf-8") as wordlistFile:
            readwordlist = open(wordlistToUse, "r",encoding="utf-8").readlines()
            counter = len(readwordlist)

            for word in wordlistFile:
                pwdtries+=1
                #sys.stdout.write(ERASE_LINE)
                h = hashlib.new(ty)
                h.update(word.strip().encode("utf-8"))
                if h.hexdigest() == hashToCrack:
                    found = True
                    clearTerminal()
                    sys.stdout.write(ERASE_LINE)
                    print(Fore.LIGHTCYAN_EX+"""
                         _             
__  _____ _ __ __ _  ___| | _____ _ __ 
\ \/ / __| '__/ _` |/ __| |/ / _ \ '__|
 >  < (__| | | (_| | (__|   <  __/ |   
/_/\_\___|_|  \__,_|\___|_|\_\___|_|   
___________--------------___________
 >> Crack Hash Wpa2 & More Ahmed Kamal
                           """+Style.RESET_ALL)
                    print('Output:')
                    print('Successfully Crack '+Fore.LIGHTGREEN_EX+'1'+Style.RESET_ALL+' Hash')
                    print()
                    print('['+Fore.LIGHTGREEN_EX+'+'+'] '+Style.RESET_ALL+'{}'.format(ty)+' {} : {}'.format(hashToCrack,word))
                    #print('\n'+'['+Fore.LIGHTGREEN_EX+'+'+Style.RESET_ALL+']'+' Hash Cracked! Password:>> '+str(word))
                    print ('['+Fore.LIGHTGREEN_EX+'+'+Style.RESET_ALL+']'+" Passwords Tried ",pwdtries)
                    print('')
                   
                    break 
                else:
                    print('start cracking: words ',pwdtries, end='\r')
                    #sys.stdout.write(ERASE_LINE)

            if found == False:
                print(
                    "\nSorry, hash couldn't be found! Please try another wordlist\n")
    except FileNotFoundError:
        print("ERROR FILE NOT FOUND! Did you put the correct wordlist file path?")
    except KeyboardInterrupt:
        print("\nQuitting Program...Have a nice day!")





            










def onlinehashcrackerapi():
    class fontcolors:
        BLUE = Fore.BLUE
        WHITE = Fore.WHITE
        GREEN = Fore.GREEN
        YELLOW = Fore.YELLOW
        RED = Fore.RED
        CYAN = Fore.CYAN
        END = '\x1b[0m'

    class symbols:
        ONE = Fore.YELLOW+'[1] '
        TWO = Fore.YELLOW+'[2] '
        THREE = Fore.YELLOW+'[3] '
        INFO = Fore.YELLOW+'[!] '
        QUE = Fore.GREEN+'[?] '
        FAIL = Fore.RED+'[-] '
        SUCCESS = Fore.GREEN+'[+] '
        INPUT = Fore.CYAN+'[>>] '

    #online-hash-crack banner   

    print( """
                  _   _               _                         _    
                 (_) | |             | |                       | |   
       __ _ _ __  _  | |__   __ _ ___| |__   ___ _ __ __ _  ___| | __
      / _` | '_ \| | | '_ \ / _` / __| '_ \ / __| '__/ _` |/ __| |/ /
     | (_| | |_) | | | | | | (_| \__ \ | | | (__| | | (_| | (__|   < 
      \__,_| .__/|_| |_| |_|\__,_|___/_| |_|\___|_|  \__,_|\___|_|\_\
           | |                                                       
           |_|                                                       
    OnlineHashCrack.com - API                          ~ BALAHA             
    """)
    print(fontcolors.END)

    #legend spotted here...hahaha
    print(f"{fontcolors.CYAN}*** Usage Instructions ***{fontcolors.END}")
    print(f"{fontcolors.CYAN}---------------------------------------------------------{fontcolors.END}")
    print(f"{symbols.ONE}{fontcolors.YELLOW}Enter Your Email :{fontcolors.END}")
    print(f"{symbols.SUCCESS}{fontcolors.WHITE}Email is needed to get the result.{fontcolors.END}")
    print(f"\n{symbols.TWO}{fontcolors.YELLOW}Enter File Path :{fontcolors.END}")
    print(f"{symbols.SUCCESS}{fontcolors.WHITE}Maximum File Size : 200 MB{fontcolors.END}")
    print(f"{symbols.SUCCESS}{fontcolors.WHITE}Supported Files Are :{fontcolors.END}")
    print(f"{symbols.SUCCESS}{fontcolors.WHITE}Wifi WPA(2): Network dumps(.cap, .pcap, .pcapng){fontcolors.END}")
    print(f"{symbols.SUCCESS}{fontcolors.WHITE}MS Office: Word, Excel or Powerpoint{fontcolors.END}")
    print(f"{symbols.SUCCESS}{fontcolors.WHITE}iTunes Backup: encrypted iTunes Backup Manifest.plist{fontcolors.END}")
    print(f"{symbols.SUCCESS}{fontcolors.WHITE}Archives: encrypted ZIP / RAR / 7-zip archives{fontcolors.END}")
    print(f"{symbols.SUCCESS}{fontcolors.WHITE}PDF: encrypted / password-protected .PDF files{fontcolors.END}")
    print(f"\n{symbols.THREE}{fontcolors.YELLOW}Price :{fontcolors.END}")
    print(f"{symbols.SUCCESS}{fontcolors.WHITE}Totally free of charge.{fontcolors.END}")
    print(f"{fontcolors.CYAN}---------------------------------------------------------{fontcolors.END}")

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    # for custom mails : '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' 

    # check email using regex
    def check_email(email):
        if(re.search(regex,email)):
            pass
        else:
            print(f"{symbols.FAIL}Invalid Email !")
            exit()

    # check if file exists or not
    def check_path(path):
        if Path(path).is_file():
            pass
        else:
            print (f"{symbols.FAIL}File Not Found !")
            exit()

    # taking user inputs
    email = input("Email> ")
    check_email(email)
    path = input("File Path> ")
    check_path(path)

    # using curl : curl -X POST -F "email=valid@email.com" -F "file=@/file/path/" https://api.onlinehashcrack.com
    files = {
        'email': (None, email),
        'file': (path, open(path, 'rb')),
    }

    # using requests post to interact with api endpoint
    try:
        response = requests.post('https://api.onlinehashcrack.com/', files=files)
        print(response.text)
        if '[-] This file extension is not supported. Please try again or contact us.' in response.text:
            print(f"{symbols.FAIL}Extension is not supported !")
            print(f"{symbols.FAIL}Please try again with another file !")
        elif '[-] File is not valid.' in response.text:
            print(f"{symbols.FAIL}Invalid file !")
            print(f"{symbols.FAIL}Please try again with another file !")
        elif '[+] This file has already been sent!' in response.text:
            print(f"{symbols.SUCCESS}File already exists !")
            print(f"{symbols.SUCCESS}This file is in cracking process !")
            print(f"{symbols.SUCCESS}Check your e-mail...")
        elif '[+] Something went wrong: this file is not password-protected OR the encryption method is not supported.' in response.text:
            print(f"{symbols.FAIL}File is not encrypted !")
            print(f"{symbols.INFO}Please send an encrypted file !")
        elif 'Yours file' and 'enters in the cracking process' in response.text:
            print(f"{symbols.SUCCESS}{fontcolors.GREEN}File Uploaded Successfully...{fontcolors.END}")
            print(f"{symbols.SUCCESS}Started 20M+ wordlist and hybrid bruteforce.")
            print(f"{symbols.SUCCESS}Check your email to see cracking status.")
            print(f"{symbols.INFO}It takes maximum 48 hours to crack a file !")
            print(f"{symbols.INFO}Sit back and relax...")
            print(f"{symbols.INFO}We will send you an email when it's done !")
        else:
            print(f"{symbols.FAIL}{fontcolors.WHITE}Please try again !{fontcolors.END}")
    except requests.exceptions.ConnectionError as err:
        print(f"{symbols.FAIL}Something Went Wrong !")
        raise SystemExit(err)



def hashidntfionlineapi(hash):
    r = requests.get('https://hashes.com/en/api/identifier?hash={}'.format(hash))
    scode = 200

    if r.status_code==scode:
        algorithm = r.text.split('"')[-4]
        ty = r.text.split('"')[-2]
        clearTerminal()
        print("[",Fore.LIGHTGREEN_EX,"+",Style.RESET_ALL,"]",' Possible {} {}'.format(algorithm,ty))
    else:
        print('ERROR reach to website! ')


def hashing(PASSWORD,algorithm):
    if algorithm=='blake2b':
        Hasher = hashlib.blake2b(PASSWORD.encode()).hexdigest() 
        print('[+] blake2b Hash')
        print()
        print(Hasher)
    elif algorithm=='sha224':
        Hasher = hashlib.sha224(PASSWORD.encode()).hexdigest() 
        print('[+] sha224 Hash')
        print()
        print(Hasher)
    elif algorithm=='sha3_224':
        Hasher = hashlib.sha3_224(PASSWORD.encode()).hexdigest() 
        print('[+] sha3_224 Hash')
        print()
        print(Hasher)
    elif algorithm=='md5':
        Hasher = hashlib.md5(PASSWORD.encode()).hexdigest() 
        print('[+] md5 Hash')
        print()
        print(Hasher)

    elif algorithm=='sha3_512':
        Hasher = hashlib.sha3_512(PASSWORD.encode()).hexdigest() 
        print('[+] sha3_512 Hash')
        print()
        print(Hasher)

    elif algorithm=='sha512':
        Hasher = hashlib.sha512(PASSWORD.encode()).hexdigest() 
        print('[+] sha512 Hash')
        print()
        print(Hasher)

    elif algorithm=='sha384':
        Hasher = hashlib.sha384(PASSWORD.encode()).hexdigest() 
        print('[+] sha384 Hash')
        print()
        print(Hasher)

    elif algorithm=='blake2s':
        Hasher = hashlib.blake2s(PASSWORD.encode()).hexdigest() 
        print('[+] blake2s Hash')
        print()
        print(Hasher)

    elif algorithm=='sha3_384':
        Hasher = hashlib.sha3_384(PASSWORD.encode()).hexdigest() 
        print('[+] sha3_384 Hash')
        print()
        print(Hasher)

    elif algorithm=='sha256':
        Hasher = hashlib.sha256(PASSWORD.encode()).hexdigest() 
        print('[+] sha256 Hash')
        print()
        print(Hasher)

    elif algorithm=='sha1':
        Hasher = hashlib.sha1(PASSWORD.encode()).hexdigest() 
        print('[+] sha1 Hash')
        print()
        print(Hasher)



def banners():
    one = Fore.LIGHTGREEN_EX+'1' +Style.RESET_ALL
    ze =  Fore.LIGHTGREEN_EX+'0' +Style.RESET_ALL
    a,l,e,r,t= 'A' , 'l' ,'e' , 'r' ,'t' 
    SYSFIL = '\n'+Fore.LIGHTGREEN_EX+"==========================="+Style.RESET_ALL
    SYSFIL += '\n'+Back.LIGHTBLACK_EX + Fore.LIGHTRED_EX+'S Y S T E M   F A I L U R E'+Style.RESET_ALL
    SYSFIL += '\n'+Fore.LIGHTGREEN_EX+'==========================='+Style.RESET_ALL
    SYSFIL += """

  {}      {}     {}       {}       
  {}      {}     {}       {}   
  {}      {}     {}       {}     
  {}      {}     {}       {} 
  {}      {}     {}       {}  
  {}      {}     {}       {}
  {}      {}     {}       {}
  {}      {}     {}       {}
  {}      {}     {}       {}
  {}      {}     {}       {}
    """.format(one,ze,one,ze,one,ze,one,ze,one,ze,one,ze,one,ze,one,ze,one,ze,one,ze,one,one,ze,one,ze,one,ze,one,ze,one,ze,one,ze,one,ze,Fore.LIGHTGREEN_EX+a,l,e,r,t+Style.RESET_ALL)
    print(SYSFIL)
    mainban = Fore.LIGHTCYAN_EX+"----------------------------------------"


def clearTerminal():
    System= os.name
    if System=='nt':
        os.system('cls')
    

    else :
        os.system('clear')

def crackhashbryteforce():
    solved = False
    ERASE_LINE = '\x1b[2K' 
    #print('['+Fore.LIGHTGREEN_EX+"*"+Style.RESET_ALL+'algorithm >> md5 sha1 sha256 sha384 sha3_512 blake2s')
    print('['+Fore.LIGHTGREEN_EX+"*"+Style.RESET_ALL+'Min Password length ')
    Min = input('Shell@MinLenth>')
    print('['+Fore.LIGHTGREEN_EX+"*"+Style.RESET_ALL+'Max Password length ')
    Max = input('Shell@MaxLenth> ')
    print(Fore.LIGHTGREEN_EX+"""
?l = 'abcdefghijklmnopqrstuvwxyz'
?u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
?d = '0123456789'
?l?d = abcdefghijklmnopqrstuvwxyz0123456789
?u?d = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
?a = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
?? = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
"""+Style.RESET_ALL)
    Chars =  input('chars> ')
    print(Fore.LIGHTMAGENTA_EX+'True '+Style.RESET_ALL+' or'+ Fore.LIGHTYELLOW_EX+' False'+Style.RESET_ALL+' recommended Fasle if True Guessing will be slow')
    verbose = input('Shell@Verbose> ')
    PASSWORD = input ('Shell@Hash>> ')
    HashSalt = input('Shell@algorithm> ')

    





    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    whitespace = ' \t\n\r\x0b\x0c'


    if Chars=="?d":
        chars = digits

    elif Chars=='?u':
        chars =  ascii_uppercase

        

    elif Chars=='?l':
        chars =  ascii_lowercase

    elif Chars=='?l?d':
        chars =  ascii_lowercase+digits

    elif Chars=='?u?d':
        chars =ascii_uppercase+digits

    elif Chars=='?a':
        chars = ascii_lowercase+ascii_uppercase+digits+punctuation

    elif Chars=='??':
        chars = printable

    else:
        print('Error: Use List chars To Show characters')

    clearTerminal()
    print('...............................................')
    print('Input Mode .................... -> Bruteforce')
    print('Input Chars ................... -> {} '.format(Chars))
    print('Min Passwords ................. -> :{}'.format(Min))
    print('Max Password .................. -> :{}'.format(Max))
    print('Salt .......................... -> {}'.format(HashSalt))
    print('Verbose ....................... -> {}'.format(verbose))
    #print('Status ... [Running]')
    sys.stdout.write('\rStatus.............. [Initializing]')
    
    sleep(3)
    sys.stdout.write(ERASE_LINE) 
    #sys.stdout.write("\033[K")
    #sys.stdout.write('\b')
    r = '['+Fore.LIGHTGREEN_EX+'Running'+Style.RESET_ALL+']'
    sys.stdout.write('\rStatus... {}'.format(r))
    print()
    starttime=time.time()
    pwdtries=0
    for length in range(int(Min),int(Max)+1): 
        to_attempt = product(chars, repeat=length)
        for attempt in to_attempt:
            x = ''.join(attempt)
            if HashSalt=='blake2b':
                h = hashlib.blake2b(x.encode()).hexdigest() 
            elif HashSalt=='sha224':
                h = hashlib.sha224(x.encode()).hexdigest() 

            elif HashSalt =='sha3_224':
                h = hashlib.sha3_224(x.encode()).hexdigest() 

            elif HashSalt=="md5":
                 h = hashlib.md5(x.encode()).hexdigest() 

            elif HashSalt=='sha3_512':
                h = hashlib.sha3_512(x.encode()).hexdigest() 

            elif HashSalt=='sha512':
                h = hashlib.sha512(x.encode()).hexdigest() 

            elif HashSalt=='sha384':
                h = hashlib.sha384(x.encode()).hexdigest() 

            elif HashSalt=='blake2s':
                h = hashlib.blake2s(x.encode()).hexdigest() 

            elif HashSalt=='sha3_384':
                h = hashlib.sha3_384(x.encode()).hexdigest() 

            elif HashSalt=='sha256':
                h = hashlib.sha256(x.encode()).hexdigest() 

            elif HashSalt=='sha1':
                h = hashlib.sha1(x.encode()).hexdigest() 
            else:
                print('['+Fore.RED+"-"+Style.RESET_ALL+'algorithm Not Found')
                sys.exit()

            hashh =  PASSWORD
            pwdtries+=1 

            Passwords_Try = str(pwdtries)
            sys.stdout.write('\rPasswords Tested '+'({})'.format(Passwords_Try)) 
            #sys.stdout.write("\033[F")

            if hashh in h:
                Cracked_Hash = x
                print('\n')
                solved = True
                ast = '['+Fore.LIGHTGREEN_EX+'+'+Style.RESET_ALL+']'
                print(ast+' Hash Cracked!: {}:{} '.format(hashh,Cracked_Hash))
                print()
                break
            else:
                if verbose=='True':
                    print('ATTACK MODE Bruteforce TRY TO FIND PASSWORD <........'+hashh+':',x)
                else:
                    pass

                
        if hashh == h:
            break
    ast = '['+Fore.LIGHTGREEN_EX+'+'+Style.RESET_ALL+']'
    Mrak = '['+Fore.RED+'!'+Style.RESET_ALL+']'
    closetime = time.time()
    if solved==True:                
        print (ast,"Starting Time ",starttime)
        print (ast,"Closing  Time ",closetime)
        print (ast,"Passwords Tried  ",pwdtries)
        print (ast,"Average Speed ",pwdtries/(closetime-starttime))
        print()
    else:
        print() 
        print(Mrak,"Cracking Failed")
        print (ast,"Starting Time ",starttime)
        print (ast,"Closing  Time ",closetime)
        print(ast,"Reached end of Words")
        print (ast,"Passwords Tried  ",pwdtries)
        print (ast,"Average Speed ",pwdtries/(closetime-starttime))
        print()





def Hashcrack():
    clearTerminal()
    banners()
    verbose = 'False'
    wordlistToUse = input('[#]Shell@Wordlist>> ')
   

    print(Fore.MAGENTA+'Wordlist> '+Style.RESET_ALL+wordlistToUse)
    hashToCrack = input('[#]Shell@Hash>> ')
   
        
    print(Fore.MAGENTA+'Hash> '+Style.RESET_ALL+hashToCrack)
    algorithmToUse = input ('[#]Shell@Algorithm>> ')
    
    print(Fore.MAGENTA+'algorithm> '+Style.RESET_ALL+algorithmToUse)
    print('[#] Verbose '+Fore.MAGENTA+'True'+Style.RESET_ALL+Fore.YELLOW+' False'+Style.RESET_ALL)
    verbose = input(str('[#]Shell@Verbose>> '))
    print(Fore.MAGENTA+'verbose> '+Style.RESET_ALL+verbose)
    pwdtries=0
    found = False
    CURSOR_UP_ONE = '\x1b[1A' 
    ERASE_LINE = '\x1b[2K' 
    try:
        with open(wordlistToUse, mode="r",encoding="utf-8") as wordlistFile:
            readwordlist = open(wordlistToUse, "r",encoding="utf-8").readlines()
            counter = len(readwordlist)
            if verbose=='False':
                print('.............................')
                print('Input Mode -> Dictionary')
                print('Hash ->'+hashToCrack)
                print('Wordlist {} Words({})'.format(wordlistToUse.split('\\')[-1],len(readwordlist)))
                print('Salt -> {}'.format(algorithmToUse))
                print('Verbose ->'+Fore.YELLOW+' {}'.format(verbose)+Style.RESET_ALL)
                sys.stdout.write('\rStatus... [Initializing]')
                print('Status ... [Running]')
                starttime=time.time()

            for word in tqdm.tqdm(wordlistFile,total=counter, unit="Word"):
                pwdtries+=1
                h = hashlib.new(algorithmToUse)
                h.update(word.strip().encode("utf-8"))
                if h.hexdigest() == hashToCrack:
                    found = True
                    
                    sys.stdout.write(ERASE_LINE)
                    
                    print('\n'+'['+Fore.LIGHTGREEN_EX+'+'+Style.RESET_ALL+']'+' Hash Cracked! Password:>> '+str(word))
                    closetime = time.time()
                    print ("[+] Starting Time ",starttime)
                    print ("[+] Closing  Time ",closetime)
                    print ("[+] Passwords Tried  ",pwdtries)
                    print ("[+] Average Speed ",pwdtries/(closetime-starttime));print()
                   
                    break 
                else:
                    if verbose =='False':
                        pass
                    else:
                        #print(Fore.LIGHTRED_EX+'[*] Try <>...H....A...<..S...H.....>.C.A.R.A.C.E.R........<> '+word.strip()+Style.RESET_ALL)
                        print('['+Fore.LIGHTRED_EX+"+"+Style.RESET_ALL+"]"+' Try.......... '+word.strip()+Style.RESET_ALL)
                
            if found == False:
                print(
                    "\nSorry, hash couldn't be found! Please try another wordlist\n")
                closetime = time.time()
                print ("[+] Starting Time ",starttime)
                print ("[+] Closing  Time ",closetime)
                print ("[+] Passwords Tried  ",pwdtries)
                print ("[+] Average Speed ",pwdtries/(closetime-starttime));print()

    except FileNotFoundError:
        print("ERROR FILE NOT FOUND! Did you put the correct wordlist file path?")
    except KeyboardInterrupt:
        print("\nQuitting Program...Have a nice day!")


def hashListCrack(wordList, hashList, algorithm):
    try:
        print(f"\nSelect {colored('ATTACK MODE', 'red')}")
        print("1. Intense attack, every hash is compared to EVERY word in the wordlist in order")
        print("2. Random attack, every hash is compared to a random word in the wordlist only once")
        print("0. Exit Hash-Cracker")
        attackMode = input(f"{colored('Hash-Cracker > ', 'green')}")
        if attackMode == "0":
            print("Have a nice day!")
            time.sleep(2)
            clearTerminal()
            exit()

        while attackMode not in ["1", "2", "3"]:
            print("INVALID CHOICE!\n")
            attackMode = input(f"{colored('Hash-Cracker > ', 'green')}")

        with open(wordList, mode="r",encoding="utf-8") as wordListFile:
            listOfWords = list(wordListFile.readlines())
            with open(hashList, mode="r") as hashListFile:
                listOfHashes = list(hashListFile.readlines())
                resultsString = ""
                hashListFile.seek(0, 0)

                if attackMode == "1":
                    for hash in hashListFile.readlines():
                        for word in listOfWords:
                            h = hashlib.new(algorithm)
                            h.update(word.strip().encode('utf-8'))
                            if hash.strip() == h.hexdigest():
                                resultsString = resultsString + f"{hash.strip()} was cracked to be {colored(word, 'green')}\n"
                                listOfHashes.remove(hash)
                            else:
                                print('try ..... {}'.format(word))

                elif attackMode == "2":
                    for hash in hashListFile.readlines():
                        wordListCopy = listOfWords[:]
                        while len(wordListCopy) != 0:
                            randomIndex = random.randint(0, len(wordListCopy)-1)
                            randomWord = wordListCopy[randomIndex]
                            h = hashlib.new(algorithm)
                            h.update(randomWord.strip().encode('utf-8'))
                            if hash.strip() == h.hexdigest():
                                resultsString = resultsString + f"{hash.strip()} was cracked to be {colored(randomWord, 'green')}\n"
                                listOfHashes.remove(hash)
                                break
                            else:
                                wordListCopy.remove(randomWord)

                print("\n" + resultsString)
                if len(listOfHashes) > 0:
                    for uncrackedHash in listOfHashes:
                        print(
                            f"{uncrackedHash.strip()} could not be cracked! Try a different wordlist? Or a different algorithm")
    except FileNotFoundError:
        print("ERROR FILE NOT FOUND! Did you put the correct wordlist file path AND the correct hashlist path?")
    except KeyboardInterrupt:
        print("\nQuitting Program...Have a nice day!")







clearTerminal()

def mainbanner():
    print(Fore.LIGHTGREEN_EX+"*"+"""
    fb:https://web.facebook.com/ahmedbalaha15485/
    ----------------------------------------------
    https://github.com/HackCode0x1
    ----------------------------------------------
                         _             
__  _____ _ __ __ _  ___| | _____ _ __ 
\ \/ / __| '__/ _` |/ __| |/ / _ \ '__|
 >  < (__| | | (_| | (__|   <  __/ |   
/_/\_\___|_|  \__,_|\___|_|\_\___|_|   
        COdeD >    Ahmed Kamal  
    """+Style.RESET_ALL+Fore.LIGHTRED_EX)
#time.sleep(3)

mainbanner()
print('>1>shell#0x2:> Crack Hash')
print('>2>shell#0x2:> Hash identifie')
print('>3>shell#0x2:> Hashing')
print('>4>shell#0x2:> Crack list of hash')
print('>5>shell#0x2:> Crack Hash Mode <<Bruteforce')
print('>6>shell#0x2:> Crack Hash Mode <<onlinehashcrackerapi')
print(Style.RESET_ALL)

print()
ch = input('shell>>> ')

if ch =='1':
    clearTerminal()
    mainbanner()
    Hashcrack()

if ch=='2':
    clearTerminal()
    mainbanner()
    Hash = input('sell@Hash >>>> ')
    hashidntfionlineapi(Hash)

if ch=='3':
    clearTerminal()
    mainbanner()
    password = input('shell@password>> ')
    algorithm = input('sell@algorithm>> ')
    hashing(password,algorithm)

if ch=='4':
    clearTerminal()
    mainbanner()
    wordlist = input('shell@wordlist>> ')
    hashfile = input('shell@hashfile>> ')
    salt = input('shell@algorithm>> ')
    hashListCrack(wordlist,hashfile,salt)

if ch=='5':
    clearTerminal()
    mainbanner()
    crackhashbryteforce()

if ch=='6':
    clearTerminal()
    mainbanner()
    onlinehashcrackerapi()




