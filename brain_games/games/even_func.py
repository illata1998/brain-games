from random import randint


def is_even(num):
    return num % 2 == 0


def question_even():
    num = randint(1, 100)
    print('Question: ' + str(num))
    return 'yes' if is_even(num) else 'no'
