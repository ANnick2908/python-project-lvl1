"""The script of programm brain_prime."""
from random import randrange

from brain_games.cli import welcome_user
from brain_games.game_logic import logic
from brain_games.scripts.brain_games import greeting


def isdivide(number, numbers):
    """Check is number divided to numbers.

    Args:
        number: number.
        numbers: list of numbers.

    Returns:
        True: number is divided to some numbers.
        False: number is not divided to all numbers.

    """
    for num in numbers:
        if number % num == 0:
            return True
            break  # noqa: WPS427
    return False


def generate_primes(size=20):
    """Generate list of prime numbers.

    Args:
        size: amount of prime numbers.

    Returns:
        primes: list of prime numbers.

    """
    primes = [2]
    numbers = [2]
    number = 2
    while len(primes) < size:
        number += 1
        if not isdivide(number, numbers):
            primes.append(number)
        numbers.append(number)
    return primes


size = 20
primes = generate_primes(size)


def instruction():
    """Print instruction."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def check_isprime(number):
    """Check is number prime or not.

    Args:
        number: number.

    Returns:
        'yes': number is prime.
        'no': number is not prime.

    """
    if number in primes:
        return 'yes'
    return 'no'


def generate_questions():
    """Select 3 random prime number for questions.

    Returns:
        questions: list of prime numbers.

    """
    questions = []
    for _ in range(3):  # noqa: WPS122
        number = randrange(2 * size)
        questions.append(number)
    return questions


def main():
    """Start the script."""
    greeting()
    instruction()
    name = welcome_user()
    questions = generate_questions()
    logic(name, questions, check_isprime)


if __name__ == '__main__':
    main()
