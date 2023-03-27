
def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    closest_vowel = None
    closest_distance = len(word)
    for i, c in enumerate(word):
        if c in vowels:
            return c
        else:
            for j, v in enumerate(vowels):
                if abs(i - word.find(v)) < closest_distance:
                    closest_distance = abs(i - word.find(v))
                    closest_vowel = v
    return closest_vowel
