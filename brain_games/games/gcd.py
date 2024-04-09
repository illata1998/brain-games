from random import randint
from brain_games.games.engine import game_engine


INIT_MESSAGE_GCD = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def gcd_answer():
    START = 1
    FINISH = 100
    num1, num2 = randint(START, FINISH), randint(START, FINISH)
    correct_answer = find_gcd(num1, num2)
    return (
        f'{num1} {num2}',
        str(correct_answer)
    )

def gcd_game():
    game_engine(gcd_answer, INIT_MESSAGE_GCD)
