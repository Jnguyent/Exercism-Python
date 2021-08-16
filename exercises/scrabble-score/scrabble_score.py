letter_score = {
    1: 'aeioulnrst',
    2: 'dg',
    3: 'bcmp',
    4: 'fhvwy',
    5: 'k',
    8: 'jx',
    10: 'qz',
}

def score(word):
    value = 0
    for x in word.lower():
        for k, v in letter_score.items():
            if x in v:
                value += k
    return value
