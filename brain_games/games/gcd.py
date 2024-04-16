from random import randint


INIT_MESSAGE_GCD = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


number1 = randint(MIN_NUMBER, MAX_NUMBER)
number2 = randint(MIN_NUMBER, MAX_NUMBER)


def find_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
           a = a % b
        else:
            b = b % a
    return a + b


def gcd_game(number1, number2):
    question = f'{number1} {number2}'
    correct_answer = str(find_gcd(number1, number2))
    return question, correct_answer
