def count_words(sentence):
    sentence = [x for x in sentence.lower().split() if x.isalnum() or x == '\'']

    print(sentence)

    word_count = {}
    for i in sentence:
        if i not in word_count:
            word_count[i] = 1
        else:
            word_count[i] += 1


    print(word_count)
    return word_count
    
count_words("one,two,three")