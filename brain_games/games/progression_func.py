from random import randint
from brain_games.games.question_func import ask_question


def progression_game(attempt_count):
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
    if attempt_count == 0:
        print('What number is missing in the progression?')
    ask_question(' '.join(map(str, progression)))
    return str(missing_item)
