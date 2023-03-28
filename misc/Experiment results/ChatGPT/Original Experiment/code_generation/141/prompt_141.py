import re

def file_name_check(file_name):
    if re.search(r"[a-zA-Z]", file_name) and re.search(r"^[a-zA-Z]+\d{0,3}\.txt|exe|dll$", file_name):
        return 'Yes'
    else:
        return 'No'