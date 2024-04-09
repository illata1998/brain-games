from random import randint
from brain_games.games.engine import game_engine


INIT_MESSAGE_PRIME = 'Answer "yes" if given number is prime. '\
    'Otherwise answer "no".'


def is_prime(num):
    if num == 2:
        return True
    if num <= 1 or num % 2 == 0:
        return False
    return all(num % i != 0 for i in range(3, int(num ** 0.5) + 1, 2))


def prime_answer():
    START = 1
    FINISH = 100
    question_num = randint(START, FINISH)
    correct_answer = 'yes' if is_prime(question_num) else 'no'
    return question_num, correct_answer


def prime_game():
    game_engine(prime_answer, INIT_MESSAGE_PRIME)
