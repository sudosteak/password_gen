import random

def gen_words(infile):
    try:
        n = int(input("how many words: "))
    except ValueError or n < 1:
        print("invalid input. please enter a positive integer above 1")
        return  
    
    words = []
    wordlist = open(infile).read().split('\n')
    
    for _ in range(n):
        word = random.choice(wordlist) + str(random.randrange(0, 9))
        words.append(word)
    
    generated_words = '-'.join(words)
    return generated_words

def pass_gen():
    infile = "./assets/wordlist.txt"
    print(gen_words(infile))

pass_gen()
