from random import randint


def is_even(num):
    return num % 2 == 0


def even_game():
    START = 1
    FINISH = 100
    INIT_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'
    question_num = randint(START, FINISH)
    correct_answer = 'yes' if is_even(question_num) else 'no'
    return INIT_MESSAGE, str(question_num), str(correct_answer)
