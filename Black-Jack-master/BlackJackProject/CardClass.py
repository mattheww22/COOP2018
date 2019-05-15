"""
- Import random
- Make list of card types and suits
- Loop randomizing both types and suits four times to get four different card values
- Assign values to CardP1, CardP2, CardD1, CardD2
- Check to see if any of the cards are the same
    If found the same, shuffle all four again until all four are different
- return CardP1, CardP2, CardD1, and CardD2
"""
from random import *


class Deck:
    def __init__(self):

        self.suits = {0: 'H', 1: 'D', 2: 'C', 3: 'S'}
        self.suitNames = {'H': 'Hearts', 'D': 'Diamonds', 'C': 'Clubs', 'S': 'Spades'}
        self.ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self.rankNames = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                  9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
        _cards = {(0, 1): 'images/ace_of_hearts.gif', (0, 2): 'images/2_of_hearts.gif',
            (0, 3): 'images/3_of_hearts.gif', (0, 4): 'images/4_of_hearts.gif',
            (0, 5): 'images/5_of_hearts.gif', (0, 6): 'images/6_of_hearts.gif',
            (0, 7): 'images/7_of_hearts.gif', (0, 8): 'images/8_of_hearts.gif',
            (0, 9): 'images/9_of_hearts.gif', (0, 10): 'images/10_of_hearts.gif',
            (0, 11): 'images/jack_of_hearts2.gif', (0, 12): 'images/queen_of_hearts2.gif',
            (0, 13): 'images/king_of_hearts2.gif',
            (1, 1): 'images/ace_of_diamonds.gif', (1, 2): 'images/2_of_diamonds.gif',
            (1, 3): 'images/3_of_diamonds.gif', (1, 4): 'images/4_of_diamonds.gif',
            (1, 5): 'images/5_of_diamonds.gif', (1, 6): 'images/6_of_diamonds.gif',
            (1, 7): 'images/7_of_diamonds.gif', (1, 8): 'images/8_of_diamonds.gif',
            (1, 9): 'images/9_of_diamonds.gif', (1, 10): 'images/10_of_diamonds.gif',
            (1, 11): 'images/jack_of_diamonds2.gif', (1, 12): 'images/queen_of_diamonds2.gif',
            (1, 13): 'images/king_of_diamonds2.gif',
            (2, 1): 'images/ace_of_clubs.gif', (2, 2): 'images/2_of_clubs.gif',
            (2, 3): 'images/3_of_clubs.gif', (2, 4): 'images/4_of_clubs.gif',
            (2, 5): 'images/5_of_clubs.gif', (2, 6): 'images/6_of_clubs.gif',
            (2, 7): 'images/7_of_clubs.gif', (2, 8): 'images/8_of_clubs.gif',
            (2, 9): 'images/9_of_clubs.gif', (2, 10): 'images/10_of_clubs.gif',
            (2, 11): 'images/jack_of_clubs2.gif', (2, 12): 'images/queen_of_clubs2.gif',
            (2, 13): 'images/king_of_clubs2.gif',
            (3, 1): 'images/ace_of_spades.gif', (3, 2): 'images/2_of_spades.gif',
            (3, 3): 'images/3_of_spades.gif', (3, 4): 'images/4_of_spades.gif',
            (3, 5): 'images/5_of_spades.gif', (3, 6): 'images/6_of_spades.gif',
            (3, 7): 'images/7_of_spades.gif', (3, 8): 'images/8_of_spades.gif',
            (3, 9): 'images/9_of_spades.gif', (3, 10): 'images/10_of_spades.gif',
            (3, 11): 'images/jack_of_spades2.gif', (3, 12): 'images/queen_of_spades2.gif',
            (3, 13): 'images/king_of_spades2.gif'}
        self.image = _cards.get((self.suit, self.rank))

        def shuffle(_cards):

            deck = _cards.shuffle

        def getCard(Num):
            cards = []
            for i in range(4):
                cards.append(choice(_cards))

            return cards