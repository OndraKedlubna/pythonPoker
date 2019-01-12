'''
Modul pro tridu reprezentujici kartu
'''

class Card:
    '''
    Trida reprezentujici kartu
    '''

    shortcuts = {'Two':'2', 'Three':'3', 'Four':'4', 'Five':'5', 'Six':'6', 'Seven':'7',
                 'Eight':'8', 'Nine':'9', 'Ten':'10', 'Jack':'J', 'Queen':'Q', 'King':'K',
                 'Ace':'A'}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def card_symbol(self):
        '''
        Metoda vracejici symbol
        '''
        if self.suit == 'Hearts':
            return 'H'
        if self.suit == 'Diamonds':
            return 'D'
        if self.suit == 'Spades':
            return 'S'
        if self.suit == 'Clubs':
            return 'C'
        return None

    def card_rank(self):
        '''
        Metoda vracejici hodnotu
        '''
        return self.shortcuts.get(self.rank)

    def __str__(self):
        return "{} {}".format(self.card_symbol(), self.card_rank())

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
