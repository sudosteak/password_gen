#!/bin/python3
from passwd_gen import gen_passwd
from usr_gen import gen_usr

def passwd_gen():
    infile = "./assets/wordlist.txt"
    print(gen_passwd(infile))

def usr_gen():
    infile = "./assets/wordlist.txt"
    print(gen_usr(infile))

choice = input("generate (u)sername, (p)assphrase, (q)uit: ").lower()
if choice == "u":
    usr_gen()
elif choice == "p":
    passwd_gen()
else:
    print("please enter a valid input")