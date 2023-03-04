import random
from enum import Enum

class Move(Enum):
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"


class Player:
    def __init__(self, name: str):
        self.name = name
        self.move = None

    def make_move(self) -> Move:
        self.move = random.choice(list(Move))
        print(f'{self.name} makes the move: {self.move.value}')

