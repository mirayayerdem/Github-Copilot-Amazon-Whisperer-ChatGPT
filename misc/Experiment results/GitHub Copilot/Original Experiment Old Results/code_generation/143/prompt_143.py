
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    words = sentence.split()
    return ' '.join([word for word in words if is_prime(len(word))])


def is_prime(n):
    """
    Given a number n, return True if it is prime, and False otherwise.
    Example:
        is_prime(1) ➞ False
        is_prime(2) ➞ True
        is_prime(3) ➞ True
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

    





