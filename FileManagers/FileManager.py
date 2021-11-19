import os
import time

extensions = {'.pcap', '.txt', '.xml', '.json', '.evtx'}


def get_filenames(path):  
    files = []
    
    for folderName, subFolders, filenames in os.walk(path):
        #print('The current folder is' + folderName)
        for subfolder in subFolders:
            #print('Subfolder of' + folderName + ':' + subfolder)
            
            for filename in filenames:
                if (os.path.splitext(filename)[1] in extensions):
                    files.append(os.path.abspath(folderName + "\\" + subfolder + "\\" + filename))
                    #print(os.path.abspath(folderName + "\\" + subfolder + "\\" + filename))
    return files


def write_log(log_message):
    current_time = time.ctime().replace(":","-")
    current_time=current_time.replace(" ", "_")
    try:
        os.makedirs('logs')
    except Exception as ex:
        print("")
    finally:
        filename = os.path.abspath('.') + "\\logs\\" + current_time + ".log"
        file = open(filename, 'w')
        for l in log_message:
            file.write(l)
            file.write("\n")
        file.close()
