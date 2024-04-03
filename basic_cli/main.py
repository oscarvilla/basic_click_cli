import click
import os

@click.command()
@click.argument('path', type=click.Path(exists=True), default=os.getcwd())
def my_command(path):
    """Processes a given path or uses the current directory by default."""
    click.echo(f"The files in the provided path are: {os.listdir(path)}")
    # print(f"The files in the provided path are: {os.listdir(path)}")

if __name__ == '__main__':
    my_command()