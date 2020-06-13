"""The logic-programm for games-scripts."""
import prompt

from brain_games.cli import welcome_user
from brain_games.games.brain_games import greeting

ROUNDS = 3


def give_correct_answer(check, question):
    """Give correct answer on the question.

    Args:
        check: check-function.
        question: question.

    Returns:
        correct_answer: correct_answer on the question.

    """
    if isinstance(check(question), bool):
        correct_answer = 'yes' if check(question) else 'no'
    else:
        correct_answer = check(question)
    return correct_answer


def logic(instruction, generator, check):  # noqa: WPS210
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
        correct_answer = give_correct_answer(check, question)
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
