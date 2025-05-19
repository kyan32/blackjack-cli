# game.py

import json
import os
from deck import Deck
from hand import Hand
from utils import clear_screen, prompt_choice, press_enter_to_continue

# Constants for available game choices and file path
GAME_CHOICES = ['hit', 'stand']
HIGHSCORE_FILE = "highscores.json"

# Load highscores from file if exists
# Return an empty list if file is missing or invalid
def load_highscores():
    if os.path.exists(HIGHSCORE_FILE):
        try:
            with open(HIGHSCORE_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return [] 
    return []

# Save highscores to file in JSON format
def save_highscores(highscores):
    with open(HIGHSCORE_FILE, 'w') as f:
        json.dump(highscores, f)

# Update highscores by adding the new score with player name
# Sort and keep top 3
def update_highscores(name, score):
    highscores = load_highscores()
    highscores.append({"name": name, "score": score})
    highscores = sorted(highscores, key=lambda x: x['score'], reverse=True)[:3]
    save_highscores(highscores)
    return highscores

# Display the current highscores
def show_highscores():
    scores = load_highscores()
    print("\n=== Top 3 Highest Scores ===")
    if not scores:
        print("No scores yet. Be the first to set a record!")
    else:
        for i, entry in enumerate(scores, 1):
            print(f"{i}. {entry['name']} - {entry['score']} chips")

# Main game loop for one full session
def play_game():
    clear_screen()
    name = input("Enter your name: ").strip() or "Anonymous"
    chips = 1000  # Starting chips
    clear_screen()
    print(f"Welcome, {name}! Challenge yourself: How many chips can you accumulate?")
    print("You start with 1000 chips. Let's begin!")
    press_enter_to_continue()

    # Repeat rounds as long as player has chips
    while chips > 0:
        clear_screen()
        print(f"Current chips: {chips}")

        # Ask player for bet amount
        while True:
            try:
                bet = int(input(f"Enter your bet (1–{chips}): "))
                if 1 <= bet <= chips:
                    break
                print(f"Bet must be between 1 and {chips}.")
            except ValueError:
                print("Please enter a valid integer.")

        # Set up and shuffle the deck
        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()

        # Deal two cards each
        for _ in range(2):
            player_hand.add_card(deck.deal_card())
            dealer_hand.add_card(deck.deal_card())

        # Check for natural Blackjack
        if player_hand.calculate_value() == 21 and len(player_hand.cards) == 2:
            print(f"\nYour cards: {player_hand}")
            print("Blackjack! You win 1.5x your bet.")
            chips += int(bet * 1.5)
            press_enter_to_continue()
            continue

        # Player's turn: hit or stand
        while True:
            print(f"\nYour cards: {player_hand}")
            print(f"Dealer's card: [{dealer_hand.cards[0]}]")
            if player_hand.calculate_value() == 21:
                print("Blackjack! You have 21.")
                break
            choice = prompt_choice("Hit or Stand? (hit/stand): ", GAME_CHOICES)
            if choice == 'hit':
                player_hand.add_card(deck.deal_card())
                if player_hand.is_bust():
                    print(f"Busted! {player_hand.calculate_value()} > 21. You lose {bet} chips.")
                    chips -= bet
                    break
            else:
                break

        # Dealer's turn if player is still in game
        if not player_hand.is_bust():
            while dealer_hand.calculate_value() < 17:
                dealer_hand.add_card(deck.deal_card())

            print(f"Dealer's card: [{dealer_hand.cards[0]}]")
            if dealer_hand.is_bust():
                print(f"Dealer busts! You win {bet} chips.")
                chips += bet
            else:
                p_val = player_hand.calculate_value()
                d_val = dealer_hand.calculate_value()
                if p_val > d_val:
                    print(f"You win! You gain {bet} chips.")
                    chips += bet
                elif p_val < d_val:
                    print(f"Dealer wins. You lose {bet} chips.")
                    chips -= bet
                else:
                    print("Push (tie). No chips won or lost.")

        # End game if out of chips
        if chips <= 0:
            print("\nYou've run out of chips! Game over.")
            press_enter_to_continue()
            update_highscores(name, chips)
            break

        # Ask if player wants to play another round
        again = prompt_choice("Play another round? (y/n): ", ['y', 'n'])
        if again == 'n':
            update_highscores(name, chips)
            print(f"\nYou leave the table with {chips} chips. Thanks for playing!")
            break
        

# Menu loop at startup
def main():
    while True:
        clear_screen()
        print("=== Blackjack Menu ===")
        print("1. Play")
        print("2. View the scoreboard")
        print("3. Exit")
        choice = prompt_choice("Select an option (1/2/3): ", ['1', '2', '3'])

        if choice == '1':
            play_game()
        elif choice == '2':
            clear_screen()
            show_highscores()
            press_enter_to_continue()
        elif choice == '3':
            print("Thanks for playing Blackjack! Goodbye.")
            break

if __name__ == '__main__':
    main()
