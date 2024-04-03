from random import randint
from brain_games.games.question_func import ask_question


def is_even(num):
    return num % 2 == 0


def even_game(attempt_count):
    START = 1
    FINISH = 100
    num = randint(START, FINISH)
    if attempt_count == 0:
        print('Answer "yes" if the number is even, otherwise answer "no".')
    ask_question(str(num))
    return 'yes' if is_even(num) else 'no'
