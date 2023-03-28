import re

def valid_date(date):
    if not date:
        return False
    match = re.search(r'^(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[01])-(19|20)\d{2}$', date)
    if match:
        month, day, year = match.groups()
        if int(month) in (1, 3, 5, 7, 8, 10, 12):
            if int(day) < 1 or int(day) > 31:
                return False
        elif int(month) in (4, 6, 9, 11):
            if int(day) < 1 or int(day) > 30:
                return False
        elif int(month) == 2:
            if int(day) < 1 or int(day) > 29:
                return False
        else:
            return False
        return True
    else:
        return False
