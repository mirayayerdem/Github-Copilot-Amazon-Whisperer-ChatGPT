import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    sentence = sentence.split()
    result = []
    for word in sentence:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)