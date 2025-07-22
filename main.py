import random

def gen_words(infile):
    word1 = random.choice(open(infile).read().split('\n')) + random.randrange(0, 9)
    word2 = random.choice(open(infile).read().split('\n')) + random.randrange(0, 9)
    word3 = random.choice(open(infile).read().split('\n')) + random.randrange(0, 9)
    word4 = random.choice(open(infile).read().split('\n')) + random.randrange(0, 9)
    word5 = random.choice(open(infile).read().split('\n')) + random.randrange(0, 9)
    word6 = random.choice(open(infile).read().split('\n')) + random.randrange(0, 9)
    generated_words = word1+"-"+word2+"-"+word3+"-"+word4+"-"+word5+"-"+word6
    return generated_words

def pass_gen():
    infile = "./assets/wordlist.txt"
    print(gen_words(infile))

pass_gen()
