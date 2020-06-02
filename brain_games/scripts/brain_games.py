"""The greeting script of programm brain_games."""

from brain_games.cli import welcome_user


def greeting():
    """Print the first greeting after start."""
    print('\nWelcome to the Brain Games!')


def main():
    """Start the package on call."""
    greeting()
    welcome_user()


if __name__ == '__main__':
    main()
