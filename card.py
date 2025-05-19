# card.py

class Card:
    """
    Represents a single playing card with a suit and rank.
    """
    SUIT_SYMBOLS = {
        'Hearts': '♥',
        'Diamonds': '♦',
        'Clubs': '♣',
        'Spades': '♠'
    }

    def __init__(self, suit: str, rank: str):
        """
        Initialize a Card object with a given suit and rank.

        :param suit: A string representing the suit (e.g., 'Hearts', 'Diamonds', 'Clubs', 'Spades')
        :param rank: A string representing the rank (e.g., 'A', '2'-'10', 'J', 'Q', 'K')
        """
        self.suit = suit  # e.g., 'Hearts'
        self.rank = rank  # e.g., '10' or 'K'

    def __str__(self) -> str:
        """
        Return a readable string representation of the card.
        For example: "A of Hearts", "10 of Spades"
        """
        return f"{self.rank}{self.SUIT_SYMBOLS.get(self.suit, '?')}"
