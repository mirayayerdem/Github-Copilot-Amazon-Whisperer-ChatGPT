import re

def foo(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    foo('03-11-2000') => True

    foo('15-01-2012') => False

    foo('04-0-2040') => False

    foo('06-04-2020') => True

    foo('06/04/2020') => False
    """
    match = re.match(r'^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(19|20)\d\d$', date)
    if match:
        month, day, year = match.groups()
        if int(month) in [4, 6, 9, 11] and int(day) > 30:
            return False
        elif int(month) == 2 and int(day) > 29:
            return False
        elif int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) > 31:
            return False
        else:
            return True
    else:
        return False
