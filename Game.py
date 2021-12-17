# 总共有52张扑克牌，13种点数
# 四种花色（黑桃♤、红桃♥、梅花♧、方块♢） #####
import random
from sys import exit

class Poker:
    def __init__(self):
        self.cards = [[face, suite] for face in "♠♥♣♦" for suite in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']]
        random.shuffle(self.cards)


class Dealer:
    def __init__(self):
        self.cards = Poker().cards

    def give_one_card(self):
        if not self.cards:
            self.cards.extend(Poker().cards)
        return self.cards.pop()


class Player:
    def __init__(self, name):
        '''
        初始化玩家对象的相关成员变量
        '''
        self.name = name
        self.score = 0
        self.points = 0
        self.cards_in_hand = []

    def init(self):
        '''
        重置计数器和手牌列表
        '''
        self.cards_in_hand = []
        self.points = 0

    # 统计现有手牌的总点数
    def total_count(self):
        point = 0
        # 将各张牌的点数相加，这里先默认A是1点，
        # 后面再进行判断是否转变为11点
        for face, suite in self.cards_in_hand:
            if suite in ['J', 'Q', 'K']:
                suite = 10
            point += suite
        '''
        判断有没有A，如果有再判断该取1点还是11点。
        如果A是第二张牌，且此时点数+10仍小于21点，
        那么可以将A视作11点进行相加，因为原来已经加了1点了，
        现在只需要再加上10点，如果不视作11点，则点数不变，
        赋值给self.points
        '''
        for card in self.cards_in_hand:
            if card[1] == 1 and point + 10 < 21:
                self.points = point + 10
            else:
                self.points = point


    def get_point(self):
        return self.points

def main():
    computer = Player("电脑")
    myself = Player("玩家")



if __name__ == "__main__":
    main()
