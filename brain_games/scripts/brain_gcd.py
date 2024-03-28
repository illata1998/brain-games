from ..gcd_func import question_gcd
from ..game import game


def main():
    init_message = 'Find the greatest common divisor of given numbers.'
    game(init_message, question_gcd)


if __name__ == '__main__':
    main()
