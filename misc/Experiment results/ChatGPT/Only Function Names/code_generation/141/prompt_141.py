import os

def file_name_check(file_name):
    if file_name == "" or file_name.startswith(".") or os.path.basename(file_name) != file_name:
        return False
    else:
        return True
