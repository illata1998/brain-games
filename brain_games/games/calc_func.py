from random import randint


INIT_MESSAGE_CALC = 'What is the result of the expression?'


def calc_answer():
    START = 1
    FINISH = 10
    
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
    return (
        f'{num1} {signs[sign_index]} {num2}',
        str(correct_answer)
    )


def calc_game(INIT_MESSAGE_CALC):
    game_engine(calc_answer, INIT_MESSAGE_CALC)
