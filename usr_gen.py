import random

def gen_usr(infile):
    wordlist = open(infile).read().split('\n')
    word= random.choice(wordlist) + str(random.randrange(0, 9999))
    return word
