from cryptography.fernet import Fernet
import os
from rich import console
from rich.console import Console
from rich.style import Style
from rich.syntax import Syntax
import msvcrt
import keyboard  # using module keyboard
import string # use this to get the alphabet
import time


Console = Console()
os.system("cls")
Console.print("Copyright 2021 by Dhruvan Kartik, OMNI.X LLC.",style="#51d6c2")
time.sleep(0.2)
Console.print("All rights reserved.",style="#51d6c2")
time.sleep(0.2)
Console.print("This file is part of the THAPBI Phytophthora ITS1 Classifier Tool (PICT),",style="#51d6c2")
time.sleep(0.2)
Console.print('and is released under the "OMNIX LICENSE". Please see the LICENSE',style="#51d6c2")
time.sleep(0.2)
Console.print("file that should have been included as part of this package., OMNI.X LLC.",style="#51d6c2")
time.sleep(0.2)
Console.print("Press ENTER to continue",style="#51d6c2")
def encrypt(Console):
    key = Fernet.generate_key()
    with open('googlekey.key', 'wb') as filekey:
        filekey.write(key)
    with open('googlekey.key', 'rb') as filekey:
    	key = filekey.read()
    fernet = Fernet(key)
    with open('Python\Base\google.py', 'rb') as file:
    	original = file.read()
    encrypted = fernet.encrypt(original)
    with open('Python\Base\google.py', 'wb') as encrypted_file:
    	encrypted_file.write(encrypted)
def run(Console):
    os.system("cd e:\Code; & C:\Python39\python.exe Python\Base\google.py")
    encrypt(Console)

def decrypt(Console):
    with open('googlekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('Python\Base\google.py', 'rb') as enc_file:
    	encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('Python\Base\google.py', 'wb') as dec_file:
    	dec_file.write(decrypted)
    run(Console)

def encryptdev(Console):
    key = Fernet.generate_key()
    with open('googlekey.key', 'wb') as filekey:
        filekey.write(key)
    with open('googlekey.key', 'rb') as filekey:
    	key = filekey.read()
    fernet = Fernet(key)
    with open('Python\Base\google.py', 'rb') as file:
    	original = file.read()
    encrypted = fernet.encrypt(original)
    with open('Python\Base\google.py', 'wb') as encrypted_file:
    	encrypted_file.write(encrypted)
    os.system("cls")
    options(Console)

def decryptdev(Console):
    with open('googlekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('Python\Base\google.py', 'rb') as enc_file:
    	encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('Python\Base\google.py', 'wb') as dec_file:
    	dec_file.write(decrypted)
    os.system("cls")
    options(Console)

def options(Console):
    x = input()
    os.system("cls")
    if x == "":
        decrypt(Console)
    elif x == "d":
        Console.print('1 For Decrypt \n2 for Encrypt \npress 3 to see raw file \npress 4 to go back', style="red")
        m = int(input("- "))
        if m == 1:
            decryptdev(Console)
        elif m == 2:
            encryptdev(Console)
        elif m == 3:
            os.system("cls")
            syntax = Syntax.from_path("Python\Base\google.py", line_numbers=True, theme="material", background_color="black")
            Console.print(syntax)
            time.sleep(5)
            redooptions(Console)
    else:
        decrypt(Console)
def redooptions(Console):
    options(Console)
options(Console)
