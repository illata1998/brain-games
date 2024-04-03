#!/user/bin/env python3


from brain_games.games.gcd_func import gcd_game
from brain_games.games.game_func import game_engine


def main():
    game_engine(gcd_game)


if __name__ == '__main__':
    main()
