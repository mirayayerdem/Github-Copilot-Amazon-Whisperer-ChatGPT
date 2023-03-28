return sorted(words, key = lambda x: (-len(set(x)), x))[0]
