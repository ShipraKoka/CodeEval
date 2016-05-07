import sys

letters = ["J", "Q", "K", "A"]

def compareNumberRank(x, y, card1, card2):
    if x > y:
        print(card1)
    elif y > x:
        print(card2)
    else:
        print("{} {}".format(card1,card2))

def compareLetterRank(x, y, card1, card2):
    if x == y:
        print("{} {}".format(card1,card2))
    elif x == "A":
        print(card1)
    elif y == "A":
        print(card2)
    elif x == "K":
        print(card1)
    elif y == "K":
        print(card2)
    elif x == "Q":
        print(card1)
    elif y == "Q":
        print(card2)
    elif x == "J":
        print(card1)
    elif y == "J":
        print(card2)


def numberOrLetter(x, y, card1, card2):
    #check if both cards are numbers
    if x and y in letters:
        compareLetterRank(x, y, card1, card2)
    #check if only one card is a letter
    elif x in letters:
        print(card1)
    elif y in letters:
        print(card2)
    #check if both cards are letters
    elif int(x) and int(y) in range(1, 11):
        compareNumberRank(int(x), int(y), card1, card2)
        

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        line = test.strip("\n").split("|")
        cards = line[0].strip(" ").split(" ")

        #first card
        cardOne = cards[0]
        rankOne = cardOne[:-1]
        suitOne = cardOne[-1]

        #second card
        cardTwo = cards[1]
        rankTwo = cardTwo[:-1]
        suitTwo = cardTwo[-1]
        
        trump = line[1].strip(" ")

        if trump == suitOne == suitTwo:
            numberOrLetter(rankOne, rankTwo, cardOne, cardTwo)
        elif trump == suitOne:
            print(cardOne)
        elif trump == suitTwo:
            print(cardTwo)
        else:
            numberOrLetter(rankOne, rankTwo, cardOne, cardTwo)
            





        
        













