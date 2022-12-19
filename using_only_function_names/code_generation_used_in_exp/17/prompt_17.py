from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parses a string containing musical notes.
    :param music_string: String containing musical notes.
    :return: List of musical notes.
    """
    notes = []
    note = ''
    for c in music_string:
        if c == 'A':
            note += c
        elif c == 'B':
            note += c
        elif c == 'C':
            note += c
        elif c == 'D':
            note += c
        elif c == 'E':
            note += c
        elif c == 'F':
            note += c
        elif c == 'G':
            note += c
        elif c == 'a':
            note += c
        elif c == 'b':
            note += c
        elif c == 'c':
            note += c
        elif c == 'd':
            note += c
        elif c == 'e':
            note += c
        elif c == 'f':
            note += c
        elif c == 'g':
            note += c
        elif c == ' ':
            notes.append(note)
            note = ''
        else:
            note += c
    notes.append(note)
    return notes


