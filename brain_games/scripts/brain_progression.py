from ..progression_func import question_progression
from ..game import game


def main():
    init_message = 'What number is missing in this progression?'
    game(init_message, question_progression)


if __name__ == '__main__':
    main()
