def is_isogram(string):
    temp = [x for x in string.lower() if x.isalpha()]
    return len(temp) == len(set(temp))
