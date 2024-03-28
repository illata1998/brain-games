from random import randint


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def question_prime():
    num = randint(1, 100)
    print('Question: ' + str(num))
    return 'yes' if is_prime(num) else 'no'
