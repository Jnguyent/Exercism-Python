def count_words(sentence):
    words = ''.join([x if x.isalnum() or x == '\'' else " " for x in sentence]) 
    words = [x.strip('\'') for x in words.lower().split()]

    word_count = {}
    for i in words:
        if i not in word_count:
            word_count[i] = 1
        else:
            word_count[i] += 1

    return word_count
