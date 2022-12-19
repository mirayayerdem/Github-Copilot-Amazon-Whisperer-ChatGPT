
def numerical_letter_grade(grades):
    """
    (list of int) -> list of str

    Return a list of letter grades for each grade in grades.

    >>> numerical_letter_grade([90, 95, 100, 80])
    ['A', 'A', 'A', 'B']
    >>> numerical_letter_grade([70, 80, 90, 100])
    ['C', 'B', 'A', 'A']
    >>> numerical_letter_grade([50, 60, 70, 80])
    ['D', 'C', 'B', 'B']
    >>> numerical_letter_grade([0, 20, 40, 60])
    ['F', 'F', 'F', 'C']
    """

    letter_grades = []

    for grade in grades:
        if grade >= 90:
            letter_grades.append('A')
        elif grade >= 80:
            letter_grades.append('B')
        elif grade >= 70:
            letter_grades.append('C')
        elif grade >= 60:
            letter_grades.append('D')
        else:
            letter_grades.append('F')

    return letter_grades

