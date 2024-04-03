from random import randint


def question_gcd():
    num1, num2 = randint(1, 100), randint(1, 100)
    print('Question: ' + str(num1) + ' ' + str(num2))
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return str(num1 + num2)
