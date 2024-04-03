from random import randint
from brain_games.games.question_func import ask_question


def yes_or_no_game(is_question):
    START = 1
    FINISH = 100
    num = randint(START, FINISH)
    ask_question(str(num))
    return 'yes' if is_question(num) else 'no'
