class Player:
    def __init__(self, name):
        self.name = name
        self.poker_num = 0
        self.poker_sum = 0
        self.score = 0
        self.cards_in_hand = []


def main():
    player1 = Player("我")
    player2 = Player("电脑")
    player1.poker_sum += 1
    player2.poker_sum += 1

if __name__ == "__main__":
    main()
