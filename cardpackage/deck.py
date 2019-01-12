'''
Modul pro tridu reprezentujici balicek
'''
import random
from cardpackage.card import Card

class Deck:
    '''
    Trida reprezentujici balicek
    '''

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
             'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        '''
        Zamichani
        '''
        random.shuffle(self.deck)

    def deal(self):
        '''
        Rozda kartu
        '''
        return self.deck.pop(0)

    def __str__(self):
        result = ""
        for i in self.deck:
            result += str(i)
            result += "\n"
        return result

    def __len__(self):
        return len(self.deck)
