# utils.py

import os

def clear_screen() -> None:
    """
    Clear the terminal screen (cross-platform).
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt_choice(prompt: str, choices: list[str]) -> str:
    """
    Prompt the user until a valid input from choices is entered.
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in choices:
            return choice
        print(f"Invalid choice. Please enter one of: {', '.join(choices)}.")


def press_enter_to_continue() -> None:
    """
    Pause execution until the user presses Enter.
    """
    input("Press Enter to continue...")
