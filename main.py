import sys
import tty
import termios
from passwd_gen import gen_passwd
from usr_gen import gen_usr

def get_single_key(prompt):
    print(prompt, end='', flush=True)
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        print()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def passwd_gen():
    infile = "./assets/wordlist.txt"
    print(gen_passwd(infile))

def usr_gen():
    infile = "./assets/wordlist.txt"
    print(gen_usr(infile))

case = "generate (U)sername or (P)assphrase: "
choice = get_single_key(case)
if choice == "U" or choice == "u":
    usr_gen()
elif choice == "P" or choice == "p":
    passwd_gen()
else:
    print("please enter a valid input")


#-- add gui