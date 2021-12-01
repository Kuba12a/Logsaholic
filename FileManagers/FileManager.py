import os
import time


def get_filenames(path, extensions):  
    file_paths = []
    
    for root, dirs, files in os.walk(path, topdown=False):
        print('Going trough folder {} ...', root)

        for file in files:
            if(file.split('.')[1] in extensions):
                file_paths.append(os.path.join(root,file))

    return file_paths


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
