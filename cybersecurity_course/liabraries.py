from random import choice
from random import shuffle
import statistics
import argparse
import sys

def main():
    #pickCoin()
    checkArgLength()

def pickCoin():
    coin = choice(["heads", "tails"])
    print(coin)
    cards = ["jack", "queen", "king"]
    shuffle(cards)
    for card in cards:
        print(card)
    print(statistics.mean([100,90]))
    try:
        print("hello, my name is ", sys.argv[1])
    except IndexError:
        print("Argument did not passed with file ")

def checkArgLength():
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few arguments")
    print("Hello ", sys.argv[1])


main()

