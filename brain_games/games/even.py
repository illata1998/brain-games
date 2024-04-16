from random import randint
from brain_games.games.engine import game_engine


INIT_MESSAGE_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


number = randint(MIN_NUMBER, MAX_NUMBER)


def even_game(number):
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer
