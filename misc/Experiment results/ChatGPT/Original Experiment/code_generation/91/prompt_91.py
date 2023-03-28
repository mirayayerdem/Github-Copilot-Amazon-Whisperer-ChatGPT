def is_bored(S):
    sentences = S.split('. ') + S.split('? ') + S.split('! ')
    return sum(1 for sentence in sentences if sentence.strip().startswith('I'))
