import click
import os
import FileManagers.PCAPManager as pcap_manager
import FileManagers.FileManager as file_manager
import FileManagers.EventDetectionManager as event_manager
import FileManagers.TXTManager as txt_manager

#main groupf to serve multiple commands 
@click.group()
def main():
    pass


#command section
@main.command()
@click.option('--path', default=[], help='Path to folders or files', multiple=True)
@click.option('--rules_string', prompt="enter rules >", help='Possible rules are:')
def event_detection(path, rules_string):
    """ Event generating detection programm """
    try:
        rules = rules_string.split(" ")  #String table with rules names
        files_to_scan = []
        for file in path:
            if os.path.isdir(file):
                for file in file_manager.get_filenames(file): #TODO naprawic
                    files_to_scan.append(file)
            elif os.path.isfile(file):
                files_to_scan.append(file)
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
    
    if pcap_manager.validate_filter(filter):
        try:
            if os.path.isfile(path):
                click.echo("PCAPs from folder "+ path + " displayed using " + filter+ " filter")
                result = pcap_manager.process_pcap(path, filter)
                pcap_manager.display_pkts(result)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
    else: click.echo("invalid filter")

    



@main.command()
@click.option('--path', default=[], help='Path to folders or files', multiple=True)
@click.option('--regex', help='Valid regular-expression in single quotes', required=True)
def text_search(path, regex):
    """ Simple programm to search for text """
    # jakaś walidacja czy to dobre regullar expression
    if txt_manager.validate_regex(regex):
        try:
            files_to_scan = []
            for file in path:
                if os.path.isdir(file):
                    for file in file_manager.get_filenames(file): #TODO naprawic
                        files_to_scan.append(file)
                elif os.path.isfile(file):
                    files_to_scan.append(file)
            txt_manager.process_files(files_to_scan,regex)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
    else: click.echo("regex incorrect")



#start of the programm
if __name__ == '__main__':
    main()
    
    
