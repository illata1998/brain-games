from random import randint


INIT_MESSAGE_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


number = randint(MIN_NUMBER, MAX_NUMBER)


def generate_round():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer
