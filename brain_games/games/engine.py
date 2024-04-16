import prompt


def game_engine(game):
    MAX_ATTEMPT_COUNT = 3
    attempt_count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{game.INIT_MESSAGE}')
    while attempt_count < MAX_ATTEMPT_COUNT:
        question_str, correct_answer = game.generate_round()
        print(f'Question: {question_str}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            attempt_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if attempt_count == MAX_ATTEMPT_COUNT:
        print(f'Congratulations, {name}!')
