import unittest
from hand import Hand
from card import Card

class TestHand(unittest.TestCase):
    def test_blackjack(self):
        hand = Hand()
        hand.add_card(Card("Spades", "A"))
        hand.add_card(Card("Hearts", "K"))
        self.assertEqual(hand.calculate_value(), 21)

if __name__ == "__main__":
    unittest.main()
