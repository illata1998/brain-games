from random import randint


INIT_MESSAGE = 'What number is missing in the progression?'
MIN_INITIAL_TERM = 1
MAX_INITIAL_TERM = 100
MIN_COMMON_DIFFERENCE = 1
MAX_COMMON_DIFFERENCE = 10
MIN_LENGTH = 5
MAX_LENGTH = 10


def generate_progression(initial_term, common_difference, length):
    progression = [initial_term]
    for i in range(length - 1):
        progression.append(progression[i] + common_difference)
    return progression


def convert_progression_into_string(progression, replaced_item_index):
    replaced_item = progression[replaced_item_index]
    progression[replaced_item_index] = '..'
    return ' '.join(map(str, progression)), str(replaced_item)


def generate_round():
    initial_term = randint(MIN_INITIAL_TERM, MAX_INITIAL_TERM)
    common_difference = randint(MIN_COMMON_DIFFERENCE, MAX_COMMON_DIFFERENCE)
    length = randint(MIN_LENGTH, MAX_LENGTH)
    replaced_item_index = randint(0, length - 1)
    progression = generate_progression(initial_term, common_difference, length)
    question, correct_answer =\
        convert_progression_into_string(progression,replaced_item_index)
    return question, correct_answer
