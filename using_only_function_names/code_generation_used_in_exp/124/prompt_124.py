
def valid_date(date):
    if len(date) != 10:
        return False
    if date[4] != '-' or date[7] != '-':
        return False
    try:
        int(date[:4])
        int(date[5:7])
        int(date[8:])
    except ValueError:
        return False
    return True





