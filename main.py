import click
import FileManagers.PCAPManager as pcap_manager
import FileManagers.FileManager as file_manager

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
@click.option('--folder-name', help='Name of the folder to scan')
def scan_folder(folder_name):
    click.echo(f"Folder {folder_name} scanned")
    data = folder_name


@main.command()
@click.option('--file-name', help='Name of the folder to scan')
def scan_file(file_name):
    click.echo(f"File {file_name} scanned")
    data = file_name

@main.command()
@click.option('--folder-name', default=None, help='Folder name to scan')
@click.option('--file-name', default=None, help='Folder name to scan')
@click.option('--load-rules', default=None, help='Folder name to scan')
def test(folder_name, file_name, load_rules):
    if(folder_name != None):
        scan_folder
    if (file_name != None):
        scan_file



@main.command()
@click.option('--rules', help='Name of the folder to scan')
def load_rules(rules):
    for r in rules:
        print(r)



if __name__ == '__main__':
    #global data
    #main()
    file_manager.get_filenames(r"C:\Users\kalus\OneDrive\Pulpit\BACKUP2-UAIM")