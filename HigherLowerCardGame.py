import random

Suit = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
Rank = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
NCards = 8 #number of turn in the game before being asked to play again

#gets card from top of deck
def getCard(deckIn):
    card = deckIn.pop()
    return card

#shuffle the deck
def shuffle(deckIn):
    deckOut = deckIn.copy()
    random.shuffle(deckOut)
    return deckOut

print("Welcome to higher or lower!")
print("Choose whether the next card is higher or lowers than the current card")
print("Getting it right adds 20 points; getting it wrong subtracts 25 points")
print("You start with 50 points")
print()

startingDeckList = []
#assigns rank, suit, and value to all cards
for s in Suit:
    for thisValue, rank in enumerate(Rank):
        cardDict = {'rank': rank, 'suit': s, 'value': thisValue + 1}
        startingDeckList.append(cardDict)
score = 50
#for the game
while True:
    print()
    gameDeckList = shuffle(startingDeckList) #calls function shuffle which shuffles
    currentCardDict = getCard(gameDeckList) #calls function getCard which gets card from top of the deck
    #these 3 assign values
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is ' + currentCardRank + ' of ' + currentCardSuit)
    print()
    for cardNumber in range(0, NCards):
        answer = input('Will the next card be higher or lower than the ' + currentCardRank + ' of '+ currentCardSuit +'? (Enter H or L): ')
        answer = answer.casefold() #forces lowercase
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        #print('Next card is:', nextCardRank+ ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score +=20
            else:
                print('Sorry, it was not higher')
                score -=15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score +=20
                print('You got it right, it was lower')
            else:
                score -=15
                print('Sorry, it was not lower')
        else:
            print('Not a valid submission')
            
        
        print('Your score is: ' + str(score))
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
    goAgain = input('To play again, press ENTER, or "q" to quit:')
    if goAgain =='q':
        break
print("OK Bye")