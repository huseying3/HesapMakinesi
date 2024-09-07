import requests

import time

from os import system as s

import colorama

from colorama import Fore, Back, Style

import os

os.system("apt-get install figlet")

os.system("clear")

banner = """       
_   ___       __   ____     __          
  / _ )__ __/ /  / / /____/ /_____ ____
 / _  / // / _ \/_  _/ __/  '_/ -_) __/
/____/\_, /_//_/ /_/ \__/_/\_\\__/_/
     /___/     
>>>>> Coded By Huseyin <<<<<<

|> GitHub = byh4cker

"""
print(banner)
print("Hesap Makinesi Sürüm = 1.0")
print("")
print("")
print("Toplamak İçin= +")
time.sleep(2)
print("Çıkarmak İçin = -")
time.sleep(2)
print("Çarpmak İçin= *")
time.sleep(2)
print("Bölmek İçin= /")
time.sleep(3)
print("")
print("")


num1 = float(input("İşleme Alınacak Sayı: "))

op = str(input("İşlemi Girin Örn:(+,-,/,*): "))

num2 = float(input("İşleme Girecek Sayı: "))

if op == '+':
  print(num1 + num2)
elif op == '-':
  print(num1 - num2)
elif op == '*':
  print(num1 * num2)
elif op == '/':
  print(num1 / num2)
elif op == '%s':
   print(num1 % num2)
elif op == '%':
   print((num1 / num2) * 100)
elif op == 'x%':
   print((num1 / 100) * num2)
else:
  print("Geçersiz İşlem")
