"""The script of programm brain_gcd."""
from random import randrange

from brain_games.game_logic import logic


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


def instruction():
    """Print instruction."""
    print('Find the greatest common divisor of given numbers.')


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


def generator(ROUNDS):
    """Generate numbers for questions.

    Args:
        ROUNDS: amount of rounds in the contest.

    Returns:
        questions: list of numbers.

    """
    questions = []
    for _ in range(ROUNDS):  # noqa: WPS122
        first_number = randrange(0, 100)
        second_number = randrange(0, 100)
        expression = '{a} {b}'.format(
            a=str(first_number),
            b=str(second_number),
        )
        questions.append(expression)
    return questions


def main():
    """Start the script."""
    logic(instruction, generator, check_gcd)


if __name__ == '__main__':
    main()
