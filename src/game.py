from enum import Enum
from typing import Optional

from src.player import Player, Move

class Result(Enum):
    DRAW = 'Draw'
    PLAYER1_WINS = 'Player 1 Wins!'
    PLAYER2_WINS = 'Player 2 Wins!'


def run_game(player1: Player, player2: Player) -> Optional[Result]:
    player1.make_move()
    player2.make_move()
    winner = None
    if player1.move == player2.move:
        winner = Result.DRAW
    elif player1.move is Move.ROCK and player2.move is Move.SCISSORS:
        winner = Result.PLAYER1_WINS
    elif player1.move is Move.SCISSORS and player2.move is Move.PAPER:
        winner = Result.PLAYER1_WINS
    elif player1.move is Move.PAPER and player2.move is Move.ROCK:
        winner = Result.PLAYER1_WINS
    else:
        winner = Result.PLAYER2_WINS

    return winner
