from ..calc_func import question_calc
from ..game import game


def main():
    init_message = 'What is the result of the expression?'
    game(init_message, question_calc)


if __name__ == '__main__':
    main()
