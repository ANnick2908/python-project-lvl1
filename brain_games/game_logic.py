"""The logic-programm for games-scripts."""
import prompt

from brain_games.cli import welcome_user
from brain_games.games.brain_games import greeting

ROUNDS = 3


def logic(instruction, generator, check):
    """Start the game-process.

    Args:
        instruction: print instruction for the contest.
        generator: generator of questions.
        check: check-function.

    """
    greeting()
    instruction()
    name = welcome_user()
    questions = generator(ROUNDS)
    amount = 1
    while amount < (ROUNDS + 1):
        question = questions[amount - 1]
        print('Question: {q}'.format(q=question))
        answer = prompt.string('Your answer: ')
        if type(check(question)) == bool:
            correct_answer = 'yes' if check(question) else 'no'
        else:
            correct_answer = check(question)
        if answer == correct_answer:
            print('Correct!')
            amount += 1
        else:
            print('{a} is wrong answer ;(. Correct answer was {b}'.format(
                a=answer,
                b=correct_answer,
            ))
            break
    if amount > ROUNDS:
        print('Congratulations, {n}!'.format(n=name))
