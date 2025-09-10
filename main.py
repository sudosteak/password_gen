from passwd_gen import gen_passwd

def passwd_gen():
    infile = "./assets/wordlist.txt"
    print(gen_passwd(infile))

passwd_gen()
#-- add gui
#-- add username gen