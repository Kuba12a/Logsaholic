'''import sys
sys.path.insert(0,'..\FileManagers')
import FileManagers.FileManager as file_manager
import os






def test_file_manager(path):
    files_list = " ".join(file_manager.get_filenames(path))
    file_manager.write_log(files_list)


test_file_manager(os.getcwd())'''