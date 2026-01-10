
# Typer, build great CLIs. Easy to code. Based on Python type hints.
# https://typer.tiangolo.com

# Typer is a library for building CLI applications that
# users will love using and developers will love creating.
# Based on Python type hints.

# Typer stands on the shoulders of a giant. Its only internal
# required dependency is Click.

# or just click alone
# Command Line Interface Creation Kit
# https://click.palletsprojects.com/en/stable/

# option values can be pulled from environment variables

# 2018 info:
# on linux sometimes the following encoding setting is necessary:
# LC_ALL=en_US.UTF-8
#
# or in script:
#
# import locale
# locale.setlocale(locale.LC_ALL, "UTF-8")

# TODO add typer example

import click


@click.command()
@click.option("-c", "--count", default=1, help="Number of greetings.")
@click.option("-n", "--name", prompt="Your name",
              help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for index in range(count):
        print("Hello %s!" % name)


if __name__ == "__main__":
    hello()
