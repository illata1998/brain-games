from random import randint


def is_prime(num):
    if num == 2:
        return True
    if num <= 1 or num % 2 == 0:
        return False
    return all(num % i != 0 for i in range(3, int(num ** 0.5) + 1, 2))


def is_even(num):
    return num % 2 == 0


def yes_or_no_game(is_func):
    START = 1
    FINISH = 100
    question_num = randint(START, FINISH)
    correct_answer = 'yes' if is_func(question_num) else 'no'
    return question_num, correct_answer


def even_game():
    INIT_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'
    question_num, correct_answer = yes_or_no_game(is_even)
    return (
        INIT_MESSAGE,
        str(question_num),
        str(correct_answer)
    )


def prime_game():
    INIT_MESSAGE = 'Answer "yes" if given number is prime. '\
        'Otherwise answer "no".'
    question_num, correct_answer = yes_or_no_game(is_even)
    return (
        INIT_MESSAGE,
        str(question_num),
        str(correct_answer)
    )
