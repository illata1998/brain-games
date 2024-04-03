from random import randint


def question_progression():
    progression = [randint(1, 100)]
    length = randint(5, 10)
    step = randint(1, 10)
    for i in range(length - 1):
        progression.append(progression[i] + step)
    pos = randint(0, length - 1)
    item = progression[pos]
    progression[pos] = '...'
    print('Question: ' + ' '.join(map(str, progression)))
    return str(item)
