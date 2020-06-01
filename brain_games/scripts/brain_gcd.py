"""The script of programm brain_gcd."""
from random import randrange

from brain_games.cli import welcome_user
from brain_games.game_logic import logic
from brain_games.scripts.brain_games import greeting


def instruction():
    """Print instruction."""
    print('Find the greatest common divisor of given numbers.')  # noqa: WPS421


def gcd(fn, sn):
    """Calculate the greatest common divisor.

    Args:
        fn: the first number.
        sn: the second number

    Returns:
        result: the greatest common divisor of numbers.

    """
    if sn == 0:
        return fn
    if fn < sn:
        fn, sn = sn, fn
    return gcd(sn, (fn % sn))


def check_gcd(expression):
    """Calculate the result of the expression.

    Args:
        expression: full expression as a string.

    Returns:
        result: the result of function 'gcd'.

    """
    numbers = expression.split()
    first_number = int(numbers[0])
    second_number = int(numbers[1])
    return str(gcd(first_number, second_number))


def generate_questions():
    """Generate numbers for questions.

    Returns:
        questions: list of numbers.

    """
    questions = []
    for _ in range(3):  # noqa: WPS122
        first_number = randrange(0, 100)  # noqa: S311
        second_number = randrange(0, 100)  # noqa: S311
        expression = '{a} {b}'.format(
            a=str(first_number),
            b=str(second_number),
            )
        questions.append(expression)
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
    logic(name, questions, check_gcd)


if __name__ == '__main__':
    main()
