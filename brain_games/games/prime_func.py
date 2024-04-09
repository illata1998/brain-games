from random import randint


def is_prime(num):
    if num == 2:
        return True
    if num <= 1 or num % 2 == 0:
        return False
    return all(num % i != 0 for i in range(3, int(num ** 0.5) + 1, 2))


def prime_game():
    START = 1
    FINISH = 100
    INIT_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question_num = randint(START, FINISH)
    correct_answer = 'yes' if is_prime(question_num) else 'no'
    return INIT_MESSAGE, str(question_num), str(correct_answer)
