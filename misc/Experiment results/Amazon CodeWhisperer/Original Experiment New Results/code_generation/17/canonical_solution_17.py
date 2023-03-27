note_map = {'o': 4, 'o|': 2, '.|': 1}
return [note_map[x] for x in music_string.split(' ') if x]
