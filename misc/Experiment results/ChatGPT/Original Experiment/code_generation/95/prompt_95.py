def check_dict_case(dict):
    if not dict:
        return False
    lower = all(key.islower() for key in dict)
    upper = all(key.isupper() for key in dict)
    return lower or upper
