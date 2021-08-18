def abbreviate(words):
    word_cleaned = ''.join(x if x.isalpha() or x == '\'' else " " for x in words)
    word_list = [x for x in word_cleaned.split()]
    acronym = ''
    
    for i in word_list:
        acronym += i[0].upper()
    return acronym