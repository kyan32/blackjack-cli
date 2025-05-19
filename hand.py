# hand.py

from card import Card

class Hand:
    """
    Manages a player’s or dealer’s hand of cards and calculates its value.
    """

    def __init__(self):
        """
        Initialize an empty hand.
        """
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Add a card to the hand.

        :param card: Card object to add.
        """
        self.cards.append(card)

    def calculate_value(self) -> int:
        """
        Calculate the best blackjack value of the hand.
        Aces can count as 1 or 11—choose the highest valid value ≤21,
        or the smallest value if all options bust.

        :return: integer point total of the hand.
        """
        values = [0]
        for card in self.cards:
            if card.rank in ['J', 'Q', 'K']:
                points = [10]
            elif card.rank == 'A':
                points = [1, 11]
            else:
                points = [int(card.rank)]
            values = [v + p for v in values for p in points]

        # Filter out busted totals
        valid_values = [v for v in values if v <= 21]
        return max(valid_values) if valid_values else min(values)

    def is_bust(self) -> bool:
        """
        Check if the hand value exceeds 21.

        :return: True if bust, False otherwise.
        """
        return self.calculate_value() > 21

    def __str__(self) -> str:
        """
        Return a string showing the cards and current value,
        e.g. "Hand: A of Hearts, 10 of Clubs (Value: 21)".
        """
        card_list = ', '.join(str(c) for c in self.cards)
        return f"[{card_list}] — Total: {self.calculate_value()}"
