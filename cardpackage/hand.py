'''
Modul pro tridu reprezentujici ruku hrace
'''

class Hand:
    '''
    Trida reprezentujici ruku
    '''

    order = {'Two':0, 'Three':1, 'Four':2, 'Five':3, 'Six':4, 'Seven':5,
             'Eight':6, 'Nine':7, 'Ten':8, 'Jack':9, 'Queen':10, 'King':11,
             'Ace':12}

    def __init__(self):
        self.cards = []
        four_f = self.__find_four
        full_f = self.__find_full_house
        three_f = self.__find_three
        twop_f = self.__find_two_pairs
        two_f = self.__find_two
        flush_f = self.__find_flush
        straight_f = self.__find_straight
        royal_f = self.__find_royal
        self.combinations = [[royal_f, 8], [four_f, 7], [full_f, 6], [flush_f, 5],
                             [straight_f, 4], [three_f, 3], [twop_f, 2], [two_f, 1]]
        self.values_list = []

    def __find_royal(self):
        return self.__find_flush() and self.__find_straight()

    def __find_four(self):
        if max(self.values_list) == 4:
            return True
        return False

    def __find_full_house(self):
        if 3 in self.values_list and 2 in self.values_list:
            return True
        return False

    def __find_flush(self):
        symbol = self.cards[0].suit
        for card in self.cards:
            if card.suit != symbol:
                return False
        return True

    def __find_straight(self):
        if self.values_list == [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]:
            return True
        for i in range(0, len(self.values_list) - 4):
            #print(self.values_list[i:i+5])
            if self.values_list[i:i+5] == [1, 1, 1, 1, 1]:
                return True
        return False

    def __find_three(self):
        if max(self.values_list) == 3:
            return True
        return False

    def __find_two_pairs(self):
        if self.values_list.count(2) == 2:
            return True
        return False

    def __find_two(self):
        if max(self.values_list) == 2:
            return True
        return False

    def add_card(self, card):
        '''
        Prida kartu
        '''
        self.cards.append(card)

    def __remove_card(self, poradi):
        '''
        Odebere kartu na danem miste - zacina se od 1
        '''
        self.cards[poradi - 1] = None

    def change_card(self, poradi, card):
        '''
        Vymeni kartu na danem miste - zacina se od 1
        '''
        self.__remove_card(poradi)
        self.cards[poradi - 1] = card

    def combination_value(self):
        '''
        Vrati hodnotu kombinace
        '''
        if len(self.cards) != 5:
            raise ValueError('Moc karet,  k tomuhle nemelo dojit')
        self.values_list = self.__values_list()
        for combination in self.combinations:
            if combination[0]():
                return combination[1]
        return 0

    def test_hand(self):
        '''
        Testovaci metoda
        '''
        print(self.combinations)

    def __values_list(self):
        values_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for card in self.cards:
            position = self.order.get(card.rank)
            values_list[position] += 1
        return values_list

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        result = "cards: "
        for card in self.cards:
            result = result + "\n  " + str(card)
        return result
