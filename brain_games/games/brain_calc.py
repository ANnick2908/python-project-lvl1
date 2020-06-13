"""The script of programm brain_calc."""
from random import choice, randrange

from brain_games.game_logic import logic


def instruction():
    """Print instruction."""
    print('What is the result of the expression?')


def check_calculation(expression):
    """Calculate the result of the expression.

    Args:
        expression: full expression as a string.

    Returns:
        result: the result of the expression.

    """
    symbols = expression.split()
    if symbols[1] == '+':
        return str(int(symbols[0]) + int(symbols[2]))
    elif symbols[1] == '-':
        return str(int(symbols[0]) - int(symbols[2]))
    elif symbols[1] == '*':
        return str(int(symbols[0]) * int(symbols[2]))


def generator(ROUNDS):
    """Generate numbers for questions.

    Args:
        ROUNDS: amount of rounds in the contest.

    Returns:
        questions: list of numbers.

    """
    questions = []
    operators = ['+', '-', '*']
    for _ in range(ROUNDS):  # noqa: WPS122
        first_number = randrange(0, 100)
        second_number = randrange(0, 100)
        expression = '{a} {o} {b}'.format(
            a=str(first_number),
            o=choice(operators),
            b=str(second_number),
        )
        questions.append(expression)
    return questions


def main():
    """Start the script."""
    logic(instruction, generator, check_calculation)


if __name__ == '__main__':
    main()
