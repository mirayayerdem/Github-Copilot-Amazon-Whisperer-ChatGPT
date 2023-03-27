
def numerical_letter_grade(grades):
    mean_grade = sum(grades) / len(grades)
    if mean_grade >= 90:
        return "A"
    elif mean_grade >= 80:
        return "B"
    elif mean_grade >= 70:
        return "C"
    elif mean_grade >= 60:
        return "D"
    else:
        return "F"
