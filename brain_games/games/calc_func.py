from random import randint


def calc_game():
    START = 1
    FINISH = 10
    INIT_MESSAGE = 'What is the result of the expression?'
    num1, num2 = randint(START, FINISH), randint(START, FINISH)
    signs = ['+', '-', '*']
    sign_index = randint(0, len(signs) - 1)
    match sign_index:
        case 0:
            correct_answer = num1 + num2
        case 1:
            correct_answer = num1 - num2
        case 2:
            correct_answer = num1 * num2
    return INIT_MESSAGE, f'{num1} {signs[sign_index]} {num2}', str(correct_answer)
