from random import randint
from brain_games.games.engine import game_engine


INIT_MESSAGE_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_answer():
    START = 1
    FINISH = 100
    question_num = randint(START, FINISH)
    correct_answer = 'yes' if question_num % 2 == 0 else 'no'
    return question_num, correct_answer


def even_game():
    game_engine(even_answer, INIT_MESSAGE_EVEN)
