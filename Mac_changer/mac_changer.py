#!/usr/bin/env python
import subprocess

interface = "wlan0" #this is interface 
new_mac = "00:11:22:33:44:77" #this is for mac address

print(" [+] Creadit : Name  : Ashutosh kumar gautam")
print(" [+] Creadit : Email : ashutoshkumargautam@protonmail.com")
print(" [+] Creadit : Blog : https://ashutoshkumargautam.blogspot.com")
print("-------------------------------------------------------------------")
print(" [+] Changing Mac address for " +  interface  + " to " +  new_mac)#this is for changing mac address for "interface"
print("-------------------------------------------------------------------")
subprocess.call(" ifconfig " +  interface  + " down ", shell=True)#ifconfig wlan0 down
subprocess.call(" ifconfig " +  interface  + " hw ether " + new_mac, shell=True)#ifconfig wlan0 hw ether 00:11:22:33:44:55
subprocess.call(" ifconfig " +  interface  + " up ", shell=True)#ifconfig wlan0 up



