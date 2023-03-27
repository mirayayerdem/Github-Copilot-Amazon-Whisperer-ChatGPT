

def remove_vowels(text):
    vowels = "aeiou"
    for i in text:
        if i in vowels:
            text = text.replace(i,"")
    return text