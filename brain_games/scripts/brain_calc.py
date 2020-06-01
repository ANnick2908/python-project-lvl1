"""The script of programm brain_calc."""
from random import choice, randrange

from brain_games.cli import welcome_user
from brain_games.game_logic import logic
from brain_games.scripts.brain_games import greeting


def instruction():
    """Print instruction."""
    print('What is the result of the expression?')  # noqa: WPS421


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


def generate_questions():
    """Generate numbers for questions.

    Returns:
        questions: list of numbers.

    """
    questions = []
    operators = ['+', '-', '*']
    for _ in range(3):  # noqa: WPS122
        first_number = randrange(0, 100)  # noqa: S311
        second_number = randrange(0, 100)  # noqa: S311
        expression = '{a} {o} {b}'.format(
            a=str(first_number),
            o=choice(operators),  # noqa: S311
            b=str(second_number),
            )
        questions.append(expression)
    return questions


def main():
    """Start the script."""
    greeting()
    instruction()
    name = welcome_user()
    questions = generate_questions()
    logic(name, questions, check_calculation)


if __name__ == '__main__':
    main()
