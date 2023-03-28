from typing import List

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.
    """
    beats = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    for note in music_string.split():
        result.append(beats[note])
    return result
