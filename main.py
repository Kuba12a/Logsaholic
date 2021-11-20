import click
import os
import scapy
import FileManagers.PCAPManager as pcap_manager
import FileManagers.FileManager as file_manager
import FileManagers.EventDetectionManager as event_manager

#main groupf to serve multiple commands 
@click.group()
def main():
    pass


#command section
@main.command()
@click.option('--path', default=[], help='Path to folders or files', multiple=True)
@click.option('--rules', prompt="enter rules >", help='Possible rules are:')
def event_detection(path, rules):
    """ Event generating detection programm """
    try:
        rules = rules.split(" ")  #String table with rules names
        files_to_scan = []
        for p in path:
            if os.path.isdir(p):
                for file in file_manager.get_filenames(p): #TODO naprawic 
                    files_to_scan.append(file)
            elif os.path.isfile(p):
                files_to_scan.append(p)
        event_manager.scan_files(files_to_scan, rules)
        click.echo("\nFiles scanned")

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)




@main.command()
@click.option('--path', help='Path to file', multiple=False, required=True)
@click.option('--filter', default='tcp', help='Valid BPF filter')
def display_captures(path, filter):
    """ Simple programm to display PCAPs """
    
    # jakaś walidacja czy to dobry filtr BPF
    try:
        if os.path.isfile(path):
            click.echo("PCAPs from folder "+ path + " displayed using " + filter+ " filter")
            result = pcap_manager.process_pcap(path, filter)
            result.summary()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)



@main.command()
@click.option('--path', default=[], help='Path to folders or files', multiple=True)
@click.option('--regex', default=None, help='Valid regular-expression')
def text_search(path, regex):
    """ Simple programm to search for text """
    # jakaś walidacja czy to dobre regullar expression
    try:
        files_to_scan = []
        for p in path:
            if os.path.isdir(p):
                for file in file_manager.get_filenames(p): #TODO naprawic 
                    files_to_scan.append(file)
            elif os.path.isfile(p):
                files_to_scan.append(p)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)




#start of the programm
if __name__ == '__main__':
    main()
    
    
