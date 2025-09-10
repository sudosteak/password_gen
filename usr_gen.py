import random

def gen_usr(infile):
    with open(infile) as f:
        wordlist = f.read().split('\n')
    word= random.choice(wordlist) + str(random.randrange(0, 9999))
    return word
