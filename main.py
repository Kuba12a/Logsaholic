import click
import FileManagers.PCAPManager as pcap_manager
import FileManagers.FileManager as file_manager

@click.group()
def main():
    pass
'''
def load_module(name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f"Module {name} loaded")
'''


@main.command()
@click.option('--folder-name', default=None, help='Folder name to scan')
@click.option('--file-name', default=None, help='Folder name to scan')
#@click.option('--load-rules', default=None, help='Folder name to scan')
def event_detection(folder_name, file_name, load_rules):
    
    try:
        rules = input("Enter rules names(white space seperated")
        rules = rules.split(" ")  #String table with rules names
        if(folder_name != None):
            print("Folder scanned")
            #scan_folder(folder_name, rules)
        if (file_name != None):
            #scan_file(file_name, rules)
            print("File scanned")
    except:
        print("Enter proper paths")


@main.command()
@click.option('--folder-name', default=None, help='Folder name to scan')
@click.option('--file-name', default=None, help='Folder name to scan')
@click.option('--filter', default=None, help='Valid BPF filter')
def display_captures(folder_name, file_name, filter):
    
    # jakaś walidacja czy to dobry filtr BPF
    try:
        if(folder_name != None):
            print("PCAPs from folder "+ folder_name + " displayed using " + filter+ " filter")
            #get_captures(folder_name, filter)
        if (file_name != None):
            #get_captures(file_name, filter)
            print("PCAP from file "+ file_name + " displayed using " + filter+ " filter")
    except:
        print("Enter proper paths and filter")



@main.command()
@click.option('--folder-name', default=None, help='Folder name to scan')
@click.option('--file-name', default=None, help='Folder name to scan')
@click.option('--regular-expression', default=None, help='Valid regular-expression')
def grep(folder_name, file_name, regular_expression):
    
    # jakaś walidacja czy to dobry filtr BPF
    try:
        if(folder_name != None):
            print("Displaying text files from "+ folder_name + " with grep and regular expression")
            #display_with_grep(folder_name, filter)
        if (file_name != None):
            #display_with_grep(file_name, filter)
            print("Displaying text file "+ file_name + " with grep and regular expression")
    except:
        print("Enter proper paths and regular expression")





if __name__ == '__main__':
    global data
    main()
    
    
