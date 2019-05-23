
# Command Line Interface Creation Kit
# https://click.palletsprojects.com/en/7.x/

# option values can be pulled from environment variables

# on linux sometimes the following encoding setting is necessary:
# LC_ALL=en_US.UTF-8
#
# or in script:
#
# import locale
# locale.setlocale(locale.LC_ALL, 'UTF-8')


import click


@click.command()
@click.option('-c', '--count', default=1, help='Number of greetings.')
@click.option('-n', '--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for index in range(count):
        print('Hello %s!' % name)


if __name__ == '__main__':
    hello()
