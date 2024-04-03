#!/user/bin/env python3


from brain_games.games.calc_func import calc_game
from brain_games.games.game_func import game_engine


def main():
    game_engine(calc_game)


if __name__ == '__main__':
    main()
