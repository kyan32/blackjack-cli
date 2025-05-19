# deck.py

import random
from card import Card

class Deck:
    """
    Represents a standard deck of 52 playing cards.
    """

    def __init__(self):
        """
        Initialize the deck with 52 cards.
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self) -> None:
        """
        Shuffle the deck in place.
        """
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        """
        Remove and return the top card of the deck.
        Raises IndexError if the deck is empty.
        """
        return self.cards.pop()
