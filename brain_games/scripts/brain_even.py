"""The main script of programm brain_even."""
from random import randrange

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greeting


def instruction():
    """Print instruction."""
    print('Answer "yes" if number even otherwise answer "no".')  # noqa: WPS421


def check(number):
    """Check is number even or not.

    Args:
        number: number.

    Returns:
        'yes': number is even.
        'no': number is not even.

    """
    if number % 2 == 0:
        return 'yes'
    return 'no'


def contest(name):
    """Ask user question is number even or not.

    Args:
        name: username.

    """
    amount = 1
    while amount < 4:
        number = randrange(0, 100)  # noqa: S311
        print('Question: {n}'.format(n=number))  # noqa: WPS421
        answer = prompt.string('Your answer: ')
        correct_answer = check(number)
        if answer == correct_answer:
            print('Correct!')  # noqa: WPS421
            amount += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'")  # noqa: WPS 421
            break
    if amount > 3:
        print('Congratulations, {n}!'.format(n=name))  # noqa: WPS 421


def main():
    """Start the package on call."""
    greeting()
    instruction()
    name = welcome_user()
    contest(name)


if __name__ == '__main__':
    main()
