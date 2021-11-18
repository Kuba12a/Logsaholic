import click

@click.group()
def main():
    pass

def load_module(name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f"Module {name} loaded")

@main.command()
@click.option('--m', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def select_mode(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

@main.command()
def scan_folder():
    folder_name = click.prompt('Foldername to scan', type=str)
    click.echo(f"Folder{folder_name} scanned")


@main.command()
def scan_file():
    file_name = click.prompt('Filename to scan', type=str)
    click.echo(f"Folder {file_name} scanned")


if __name__ == '__main__':
    main()