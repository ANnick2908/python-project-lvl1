"""The logic-programm for games-scripts."""
import prompt


def logic(name, questions, check):
    """Start the game-process.

    Args:
        name: username.
        questions: list of questions.
        check: check-function.

    """
    amount = 1
    while amount < 4:
        question = questions[amount - 1]
        print('Question: {q}'.format(q=question))  # noqa: WPS421
        answer = prompt.string('Your answer: ')
        correct_answer = check(question)
        if answer == correct_answer:
            print('Correct!')  # noqa: WPS421
            amount += 1
        else:
            print("{a} is wrong answer ;(. Correct answer was {b}".format(a=answer, b=correct_answer))  # noqa: WPS 421
            break
    if amount > 3:
        print('Congratulations, {n}!'.format(n=name))  # noqa: WPS 421
