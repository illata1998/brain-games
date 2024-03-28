from random import randint


def question_even():
    num = randint(1, 100)
    print('Question: ' + str(num))
    return 'yes' if is_even(num) else 'no'
