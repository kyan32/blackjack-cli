# 🃏 Blackjack CLI

A simple, modular command-line Blackjack game written in Python.

## 🎯 Features

- Play classic Blackjack against the dealer
- Modular design: `Card`, `Deck`, `Hand`, and `Game` components
- Dynamic point calculation for A (1 or 11)
- Highscore tracking with `highscores.json`
- Input validation, bet handling, and chip management

## 📂 Project Structure

```
blackjack-cli/
├── game.py             # Main game loop and UI logic
├── card.py             # Card class with suit/rank and display
├── deck.py             # Deck class: shuffling and dealing
├── hand.py             # Hand class: card management and score calc
├── utils.py            # Utility functions (input, clear screen, etc.)
├── highscores.json     # JSON file storing top scores
├── .gitignore          # Ignore pycache, venv, and temp files
├── README.md           # This file
```

## ✨ Gameplay Rules (Implemented)

- Each player starts with **1000 chips**
- Bet before each round (min 1 chip)
- **Blackjack (A + 10)** pays **1.5x** the bet
- **Bust** if hand value > 21
- Aces count as 11 or 1 based on total value
- Dealer draws until **17 or more**
- Push (tie) if player and dealer have same score

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/blackjack-cli.git
cd blackjack-cli
```

### 2. Run the game

```bash
python game.py
```

> Requires **Python 3.7+**

## 📄 License

MIT License. Feel free to fork and contribute!

---

Have fun beating the dealer!
