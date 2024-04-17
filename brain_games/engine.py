import prompt


MAX_ROUND_COUNT = 3


def run_game(game):
    round_count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.INIT_MESSAGE)
    while round_count < MAX_ROUND_COUNT:
        question_str, correct_answer = game.generate_round()
        print(f'Question: {question_str}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            round_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if round_count == MAX_ROUND_COUNT:
        print(f'Congratulations, {name}!')
