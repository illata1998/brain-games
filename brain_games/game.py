import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game(init_message, question):
    name = welcome_user()
    print(init_message)
    for i in range(3):
      correct_answer = question()
      answer = prompt.string('Your answer: ')
      if answer == correct_answer:
        print('Correct!')
        if i == 2:
          print(f'Congratulations, {name}!')
      else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        break
