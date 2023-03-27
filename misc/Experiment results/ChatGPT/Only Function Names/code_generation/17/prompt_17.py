from typing import List


def parse_music(music_string: str) -> List[int]:
    return list(map(int, music_string.split(',')))
