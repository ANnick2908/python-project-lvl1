"""Greeting program for main package."""
import prompt


def welcome_user():
    """Ask username and greet.

    Returns:
           name: username.

    """
    name = prompt.string('May I have your name? ')
    print('Hello, {n}!'.format(n=name))  # noqa: WPS421
    return name
