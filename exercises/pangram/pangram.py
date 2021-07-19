# Method to determine if a sentence is a pangram
# a pangram is a sentence that uses each letter of the alphabet at LEAST once
def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
   
    for char in alphabet:
        if char not in sentence:
            return False

    return True
