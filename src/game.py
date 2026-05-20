import random


MOVES = ("rock", "paper", "scissors")

WINNING_MOVE = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

PLAYER_WIN = "You win!"
COMPUTER_WIN = "Computer wins!"
DRAW = "Draw!"


def choose_computer_move():
    # TODO 5: Choose a random item from MOVES.
    return "rock"


def decide_winner(player_move, computer_move):
    # TODO 6: Return DRAW if both moves are the same.

    # TODO 7: Return PLAYER_WIN if WINNING_MOVE[player_move] beats computer_move.

    return "Round played."


def reset_score():
    return {"player": 0, "computer": 0}


def update_score(score, result):
    # TODO 8: Add one point to the correct side after each round.
    return
