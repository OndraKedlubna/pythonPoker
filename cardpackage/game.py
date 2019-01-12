'''
Modul pro tridu reprezentujici hru
'''

from cardpackage.hand import Hand
from cardpackage.deck import Deck

#vymen karty
#validuj vstup - retezec s menenim karet napr. 235
#zobraz vysledek

def get_input(text):
    '''
    Funkce ziskavajici input. Je vne tridy kvuli mocku.
    '''
    return input(text)

class Game:
    '''
    Trida reprezentujici hru
    '''

    def __init__(self):
        self.hand = Hand()
        self.deck = Deck()
        self.changes = []
        for _ in range(0, 5):
            self.hand.add_card(self.deck.deal())

    def play_game(self):
        '''
        Metoda na zahrani hry
        '''
        print(self.hand)
        self.change_card()
        print(self.hand)
        print("Tvoje vysledna kombinace ma hodnotu: {}".format(self.hand.combination_value()))

    def change_card(self):
        '''
        Metoda menici karty. Ocekava cisla menenych karet - napr. 123
        '''
        while True:
            input_change = get_input("Ktere karty chces vymenit?")
            if self.__validate_input(input_change, 3, 5):
                print("Menis karty: {}".format(self.changes))
                break
        self.change_execution()

    def change_execution(self):
        '''
        Provedeni vymeny
        '''
        for i in self.changes:
            new_card = self.deck.deal()
            print("dostavas cartu :{}".format(new_card))
            self.hand.change_card(i, new_card)


    def __validate_input(self, value, maximum, cards):
        if len(value) > maximum:
            return False
        values = []
        for i in value:
            try:
                k = int(i)
                if k > cards:
                    return False
                values.append(k)
            except ValueError:
                return False
        if len(values) > len(set(values)):
            return False
        self.changes = values
        return True
