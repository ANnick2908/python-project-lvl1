"""The main script of programm brain_games."""

from brain_games.cli import welcome_user


def greeting():
    """Print the first greeting after start."""
    print('Welcome to the Brain Games!')  # noqa: WPS421


def main():
    """Start the package on call."""
    greeting()
    welcome_user()


if __name__ == '__main__':
    main()
