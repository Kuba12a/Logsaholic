import click
import FileManagers.PCAPManager as pcap_manager
import FileManagers.FileManager as file_manager
import FileManagers.EventDetectionManager as event_manager


@click.group()
def main():
    pass



@main.command()
@click.option('--folder-name', default=None, help='Folder name to scan')
@click.option('--file-name', default=None, help='File name to scan')
def event_detection(folder_name, file_name):
    
    try:
        rules = input("Enter rules names (white space seperated)\n")
        rules = rules.split(" ")  #String table with rules names
        files_to_scan = []

        if(folder_name != None):
            files_to_scan = file_manager.get_filenames(folder_name)
            event_manager.scan_files(files_to_scan, rules)
            print("\nFiles scanned")

        if (file_name != None):
            files_to_scan.append(file_name)
            event_manager.scan_files(files_to_scan, rules)
            print("\nFile scanned")

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)




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
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)



@main.command()
@click.option('--folder-name', default=None, help='Folder name to scan')
@click.option('--file-name', default=None, help='Folder name to scan')
@click.option('--regular-expression', default=None, help='Valid regular-expression')
def grep(folder_name, file_name, regular_expression):
    
    # jakaś walidacja czy to dobre regullar expression
    try:
        if(folder_name != None):
            print("Displaying text files from "+ folder_name + " with grep and regular expression")
            #display_with_grep(folder_name, regular_expression)
        if (file_name != None):
            #display_with_grep(file_name, regular_expression)
            print("Displaying text file "+ file_name + " with grep and regular expression")
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)





if __name__ == '__main__':
    main()
    
    
