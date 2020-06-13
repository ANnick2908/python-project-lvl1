"""The script of programm brain_even."""
from random import randrange

from brain_games.game_logic import logic


def instruction():
    """Print instruction."""
    print('Answer "yes" if number even otherwise answer "no".')


def check_even(number):
    """Check is number even or not.

    Args:
        number: number.

    Returns:
        True: number is even.
        False: number is not even.

    """
    if number % 2 == 0:
        return True
    return False


def generator(ROUNDS):
    """Generate numbers for questions.

    Args:
        ROUNDS: amount of rounds in the contest.

    Returns:
        questions: list of numbers.

    """
    questions = []
    for _ in range(ROUNDS):  # noqa: WPS122
        number = randrange(0, 100)
        questions.append(number)
    return questions


def main():
    """Start the script."""
    logic(instruction, generator, check_even)


if __name__ == '__main__':
    main()
