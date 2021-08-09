def is_isogram(string):
    temp = ''.join(x.lower() for x in string if x.isalpha())
    
    return len(temp) == len(set(temp))
