from random import randint


def question_calc():
    num1, num2 = randint(1, 10), randint(1, 10)
    signs = ['+', '-', '*']
    i = randint(0, 2)
    print('Question: ' + str(num1) + ' ' + signs[i] + ' ' + str(num2))
    match i:
        case 0:
            return str(num1 + num2)
        case 1:
            return str(num1 - num2)
        case 2:
            return str(num1 * num2)
