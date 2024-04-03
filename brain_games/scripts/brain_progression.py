#!/user/bin/env python3


from brain_games.games.progression_func import progression_game
from brain_games.games.game_func import game_engine


def main():
    game_engine(progression_game)


if __name__ == '__main__':
    main()
