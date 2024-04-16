from random import randint
from brain_games.games.engine import game_engine


INIT_MESSAGE_PROGRESSION = 'What number is missing in the progression?'
MIN_FIRST_ELEMENT = 1
MAX_FIRST_ELEMENT = 100
MIN_STEP = 1
MAX_STEP = 10
MIN_LENGTH = 5
MAX_LENGTH = 10


first_element = randint(MIN_FIRST_ELEMENT, MAX_FIRST_ELEMENT)
step = randint(MIN_STEP, MAX_STEP)
length = randint(MIN_LENGTH, MAX_LENGTH)
missing_item_index = randint(length)


def generate_progression(first_element, step, length):
    progression = [first_element]
    for i in range(length - 1):
        progression.append(progression[i] + step)
    return progression


def generate_progression_question(progression, missing_item_index):
    missing_item = progression[missing_item_index]
    progression[missing_item_index] = '..'
    return ' '.join(map(str, progression)), str(missing_item)


def progression_game():
    game_engine(generate_progression_question, INIT_MESSAGE_PROGRESSION)
