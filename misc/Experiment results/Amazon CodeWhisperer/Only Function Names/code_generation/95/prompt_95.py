
def check_dict_case(dict):
    for key in dict:
        if key.islower():
            return False
    return True
