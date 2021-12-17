import random
from sys import exit

class Poker:
    def __init__(self):
        self.cards = [[face, suite] for face in "♠♥♣♦" for suite in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']]
        random.shuffle(self.cards)

poker = Poker()
for i in range(52):
    point = (str)(poker.cards[i][0]) + str(poker.cards[i][1])
    print(point)
print(poker.cards)
print(len(poker.cards))