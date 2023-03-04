import csv
import random
from typing import Sequence, Optional


def generate_random_name(possible_names: Sequence=[], additional_name: Optional[str] = None) -> str:
    file = open('player_names.csv', 'r')
    read_file = csv.DictReader(file)
    possible_names = [row['name'] for row in read_file]
    if additional_name:
        possible_names.append(additional_name)

    return random.choice(possible_names)


if __name__ == '__main__':
    print(generate_random_name(additional_name='chris'))