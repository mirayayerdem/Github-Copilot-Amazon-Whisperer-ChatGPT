
def numerical_letter_grade(grades):
    """Converts a numerical grade to a letter grade."""
    if grades >= 90:
        return "A"
    elif grades >= 80:
        return "B"
    elif grades >= 70:
        return "C"
    elif grades >= 60:
        return "D"
    else:
        return "F"
        