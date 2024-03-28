from ..prime_func import question_prime
from ..game import game


def main():
    init_message = 'Answer "yes" if the number is prime, otherwise answer "no".'
    game(init_message, question_prime)


if __name__ == '__main__':
    main()
