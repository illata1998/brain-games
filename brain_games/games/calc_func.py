from random import randint
from brain_games.games.question_func import ask_question


def calc_game(attempt_count):
    START = 1
    FINISH = 10
    num1, num2 = randint(START, FINISH), randint(START, FINISH)
    math_signs = ['+', '-', '*']
    math_sign_index = randint(0, len(math_signs) - 1)
    if attempt_count == 0:
        print('What is the result of the expression?')
    ask_question(f'{num1} {math_signs[math_sign_index]} {num2}')
    match math_sign_index:
        case 0:
            return str(num1 + num2)
        case 1:
            return str(num1 - num2)
        case 2:
            return str(num1 * num2)
