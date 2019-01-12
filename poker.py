from cardpackage.card import Card
from cardpackage.hand import Hand
from cardpackage.deck import Deck
from cardpackage.game import Game

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
actions = {'h': 'Hit', 's': 'Stay'}
answers = ('a', 'n')

playing = True

game = Game()
game.play_game()


#hand = Hand()
#deck = Deck()
#hand.add_card(deck.deal())
#hand.add_card(deck.deal())
#hand.add_card(deck.deal())
#hand.add_card(deck.deal())
#hand.add_card(deck.deal())
#print(hand)
#print(hand.combination_value())
