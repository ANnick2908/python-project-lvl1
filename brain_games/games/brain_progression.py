"""The script of programm brain_progression."""
from random import randrange

from brain_games.cli import welcome_user
from brain_games.game_logic import logic
from brain_games.games.brain_games import greeting


def instruction():
    """Print instruction."""
    print('What number is missing in the progression?')


def check_progression(expression):
    """Calculate the hidden element of the progression.

    Args:
        expression: full progression as a string.

    Returns:
        result: the hidden element.

    """
    progression = expression.split()
    hidden_index = progression.index('..')
    if hidden_index >= 5:
        diff = int(progression[1]) - int(progression[0])
        hidden_element = int(progression[hidden_index - 1]) + diff
    else:
        diff = int(progression[9]) - int(progression[8])
        hidden_element = int(progression[hidden_index + 1]) - diff
    return str(hidden_element)


def generate_questions():
    """Generate progression for questions.

    Returns:
        questions: list of progressions.

    """
    questions = []
    progression_size = 10
    for _ in range(3):  # noqa: WPS122
        delta = randrange(progression_size + 1)
        step = randrange(1, progression_size + 1)
        progression = [
            (_ + delta) for _ in range(0, 1000, step)
        ]
        progression = progression[:progression_size]
        progression[randrange(0, progression_size)] = '..'
        questions.append(' '.join(str(_) for _ in progression))
    return questions


def main():
    """Start the script."""
    greeting()
    instruction()
    name = welcome_user()
    questions = generate_questions()
    logic(name, questions, check_progression)


if __name__ == '__main__':
    main()
