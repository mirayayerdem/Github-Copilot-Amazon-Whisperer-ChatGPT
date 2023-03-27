
def check_dict_case(d):
    for key in d:
        if not key.islower():
            return False
    return True
