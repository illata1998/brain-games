from random import randint
from brain_games.games.question_func import ask_question


def find_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def gcd_game(attempt_count):
    START = 1
    FINISH = 100
    num1, num2 = randint(START, FINISH), randint(START, FINISH)
    if attempt_count == 0:
        print('Find the greatest common divisor of given numbers.')
    ask_question(f'{num1} {num2}')
    return str(find_gcd(num1, num2))
