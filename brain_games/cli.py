"""Greeting program for main package."""
import prompt


def welcome_user():
    """Ask username and greet.

    Returns:
           name: username.

    """
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {n}!\n'.format(n=name))
    return name
