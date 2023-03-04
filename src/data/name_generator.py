import csv
import pathlib
import random


DIR_PATH = pathlib.Path(__file__).resolve().parent

def generate_random_name() -> str:
    with open(DIR_PATH / 'player_names.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        names = [row['name'] for row in reader]
        return random.choice(names)