
def fruit_distribution(s, n):
    fruits_per_person = s // n
    remainder = s % n
    return fruits_per_person, remainder
