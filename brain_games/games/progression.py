from random import randint


INIT_MESSAGE = 'What number is missing in the progression?'
MIN_FIRST = 1
MAX_FIRST = 100
MIN_STEP = 1
MAX_STEP = 10
MIN_LENGTH = 5
MAX_LENGTH = 10


def generate_progression(first, step, length):
    progression = [first]
    for i in range(length - 1):
        progression.append(progression[i] + step)
    return progression


def remove_item(progression, removed_item_index):
    removed_item = progression[removed_item_index]
    progression[removed_item_index] = '..'
    return ' '.join(map(str, progression)), removed_item


def generate_round():
    first = randint(MIN_FIRST, MAX_FIRST)
    step = randint(MIN_STEP, MAX_STEP)
    length = randint(MIN_LENGTH, MAX_LENGTH)
    removed_item_index = randint(0, length - 1)
    progression = generate_progression(first, step, length)
    question, correct_answer = remove_item(progression, removed_item_index)
    return question, correct_answer
