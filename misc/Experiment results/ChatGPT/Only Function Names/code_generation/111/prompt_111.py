from collections import Counter

def histogram(test):
    hist = Counter(test)
    for key, value in hist.items():
        print(f'{key}: {"*" * value}')
