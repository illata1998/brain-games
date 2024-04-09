from random import randint
from brain_games.games.engine import game_engine


INIT_MESSAGE_PROGRESSION = 'What number is missing in the progression?'


def progression_answer():
    START = 1
    FINISH = 100
    MIN_LENGTH = 5
    MAX_LENGTH = 10
    MIN_STEP = 1
    MAX_STEP = 10 
    progression = [randint(START, FINISH)]
    progression_length = randint(MIN_LENGTH, MAX_LENGTH)
    step = randint(MIN_STEP, MAX_STEP)
    for i in range(progression_length - 1):
        progression.append(progression[i] + step)
    missing_item_index = randint(0, progression_length - 1)
    missing_item = progression[missing_item_index]
    progression[missing_item_index] = '..'
    return (
        INIT_MESSAGE,
        ' '.join(map(str, progression)),
        str(missing_item)
    )


def progression_game():
    game_engine(progression_answer, INIT_MESSAGE_PROGRESSION)
