from src.game import run_game
from src.data.name_generator import generate_random_name
from src.player import Player


def main():
    player1_name = generate_random_name()
    player2_name = generate_random_name()
    player1 = Player(name=player1_name)
    player2 = Player(name=player2_name)

    result = run_game(player1=player1, player2=player2)

    print(result.value)


if __name__ == '__main__':
    main()