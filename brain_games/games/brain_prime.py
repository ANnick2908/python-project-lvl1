"""The script of programm brain_prime."""
from random import randrange

from brain_games.game_logic import logic


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


def check_prime(number):
    """Check is number prime or not.

    Args:
        number: number.

    Returns:
        True: number is prime.
        False: number is not prime.

    """
    if number in primes:
        return True
    return False


def generator(ROUNDS):
    """Select 3 random prime number for questions.

    Args:
        ROUNDS: amount of rounds in the contest.

    Returns:
        questions: list of prime numbers.

    """
    questions = []
    for _ in range(ROUNDS):  # noqa: WPS122
        number = randrange(2, 2 * size)
        questions.append(number)
    return questions


def main():
    """Start the script."""
    logic(instruction, generator, check_prime)


if __name__ == '__main__':
    main()
