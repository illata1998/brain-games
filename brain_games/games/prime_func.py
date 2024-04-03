from random import randint
from brain_games.games.question_func import ask_question


def is_prime(num):
    if num == 2:
        return True
    if num <= 1 or num % 2 == 0:
        return False
    return all(num % i != 0 for i in range(3, int(num ** 0.5) + 1, 2))


def prime_game(attempt_count):
    START = 1
    FINISH = 100
    num = randint(START, FINISH)
    if attempt_count == 0:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    ask_question(str(num))
    return 'yes' if is_prime(num) else 'no'
