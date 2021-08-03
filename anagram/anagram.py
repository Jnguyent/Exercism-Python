def find_anagrams(word, candidates):
    sorted_word = sorted(word.lower())
    return [x for x in candidates if sorted_word == sorted(x.lower()) and word.lower() != x.lower()]
