import sys
import random

with open('words.txt', 'r') as words:
    text = words.readlines()
    k = int(sys.argv[1])
    pswrdlist = random.sample(text, k)
    pswrd = ''
    for element in pswrdlist:
        pswrd = pswrd + element.partition('\n')[0].capitalize()
    print(pswrd)
