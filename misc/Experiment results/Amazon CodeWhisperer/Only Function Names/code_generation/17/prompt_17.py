from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a music string into a list of notes.
    """
    notes = []
    for note in music_string.split():
        if note.isdigit():
            notes.append(int(note))
    return notes


