from src.game import run_game
from src.player import Player, Move


def test_game_determines_correct_winner():
    player1 = Player(name='foo')
    player2 = Player(name='bar')

    subject = run_game(player1=player1, player2=player2)
