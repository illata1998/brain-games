#!/user/bin/env python3


from brain_games.games.even_and_prime_func import even_game
from brain_games.games.game_func import game_engine


def main():
    game_engine(even_game)


if __name__ == '__main__':
    main()
