#!/usr/bin/env python3
import click
from commands.volume import volume


@click.group()
def main():
    pass


main.add_command(volume)


if __name__ == '__main__':
    main()
