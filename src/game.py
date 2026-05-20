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
    return random.choice(MOVES)


def decide_winner(player_move, computer_move):
    if player_move == computer_move:
        return DRAW

    if WINNING_MOVE[player_move] == computer_move:
        return PLAYER_WIN

    return COMPUTER_WIN


def reset_score():
    return {"player": 0, "computer": 0}


def update_score(score, result):
    if result == PLAYER_WIN:
        score["player"] += 1
    elif result == COMPUTER_WIN:
        score["computer"] += 1
