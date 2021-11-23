import re

def process_files(file_list,regex):
    for f in file_list:
        with open(f,"r") as file:
            for line in file:
                if re.search(regex, line):
                    print(line)

def validate_regex(regex):
    if ' ' in regex: 
        return False
    try:
        re.compile(regex)
    except re.error:
        return False
    return True