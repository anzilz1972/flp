##########################################
####author:Anzilz1972
####date: 2026-3-16
####Python编程：Fluent Python 练习 
####第一章：示例 1-1
##########################################
from collections import namedtuple

Card = namedtuple('Card',['rank','suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks ]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __repr__(self):
        return 'FrenchDeck Object'
    
def main():
    ### 生成FrenchDeck对象
    deck = FrenchDeck()
    ###打印整个套牌
    for card in deck:
        print(card)
    print("\n" + "=" * 50)
    ###反向打印整个套牌
    for card in reversed(deck):
        print(card)
    print("\n" + "=" * 50)

    ###按花色定义四个切片对象，之后生成四个花色的套牌
    ###之后打印这四个套牌
    Cards_Spades = slice(0,13)
    cards_spades = deck[Cards_Spades]

    Cards_Diamonds = slice(13,26)
    cards_Diamonds = deck[Cards_Diamonds]

    Cards_Clubs = slice(26,39)
    cards_clubs = deck[Cards_Clubs]

    Cards_Heart = slice(39,52)
    cards_hearts = deck[Cards_Heart]
    for card in cards_spades:
        print(card)
    print("\n" + "=" * 50)

    for card in cards_Diamonds:
        print(card)
    print("\n" + "=" * 50)

    for card in cards_clubs:
        print(card)
    print("\n" + "=" * 50)

    for card in cards_hearts:
        print(card)
    print("\n" + "=" * 50)


    ###按大小打印套牌
    for idx in range(13):
        cards = deck[idx::13]
        for card in cards:
            print(card)
        print("\n" + "=" * 50)

if __name__ == '__main__':
    main()
    

    





