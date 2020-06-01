"""The script of programm brain_even."""
from random import randrange

from brain_games.cli import welcome_user
from brain_games.game_logic import logic
from brain_games.scripts.brain_games import greeting


def instruction():
    """Print instruction."""
    print('Answer "yes" if number even otherwise answer "no".')  # noqa: WPS421


def check_even(number):
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


def generate_questions():
    """Generate numbers for questions.

    Returns:
        questions: list of numbers.

    """
    questions = []
    for _ in range(3):  # noqa: WPS122
        number = randrange(0, 100)  # noqa: S311
        questions.append(number)
    return questions


def main():
    """Start the script."""
    print()  # noqa: WPS421
    greeting()
    instruction()
    print()  # noqa: WPS421
    name = welcome_user()
    questions = generate_questions()
    print()  # noqa: WPS421
    logic(name, questions, check_even)


if __name__ == '__main__':
    main()
