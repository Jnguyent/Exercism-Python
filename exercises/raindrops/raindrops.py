def convert(number):

    sounds = ""

    if number % 3 == 0:
        sounds = "Pling"
    if number % 5 == 0:
        sounds = sounds + 'Plang'
    if number % 7 == 0:
        sounds = sounds + 'Plong'
    if (number % 3 != 0 and number % 5 != 0 and number % 7 != 0):
        return f'{number}'

    return sounds   