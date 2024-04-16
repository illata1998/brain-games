from random import randint, choice


INIT_MESSAGE = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
SIGNS = ['+', '-', '*']


def generate_round():
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    sign = choice(SIGNS)
    question = f'{number1} {sign} {number2}'
    match sign:
        case '+':
            correct_answer = str(number1 + number2)
        case '-':
            correct_answer = str(number1 - number2)
        case '*':
            correct_answer = str(number1 * number2)
    return question, correct_answer
