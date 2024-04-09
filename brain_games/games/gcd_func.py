from random import randint


def find_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def gcd_game():
    START = 1
    FINISH = 100
    INIT_MESSAGE = 'Find the greatest common divisor of given numbers.'
    num1, num2 = randint(START, FINISH), randint(START, FINISH)
    correct_answer = find_gcd(num1, num2)
    return (
        INIT_MESSAGE,
        f'{num1} {num2}',
        str(correct_answer)
    )
