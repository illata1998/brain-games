from brain_games.games.yes_or_no_func import yes_or_no_game


def is_even(num):
    return num % 2 == 0


def even_game(attempt_count):
    if attempt_count == 0:
        print('Answer "yes" if the number is even, otherwise answer "no".')
    return yes_or_no_game(is_even)
