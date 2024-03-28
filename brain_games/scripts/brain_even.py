#!/user/bin/env python3


from ..even_func import question_even
from ..game import game


def main():
    init_message = 'Answer "yes" if the number is even, otherwise answer "no".'
    game(init_message, question_even)


if __name__ == '__main__':
    main()
