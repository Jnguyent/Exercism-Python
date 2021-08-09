def algorithm(number):
    if number % 2 == 0:
        return number / 2
    else:
        return number * 3 + 1

def steps(number):
    if number <= 0:
        raise ValueError('Number must be a positive integer')

    step = 0
    while number != 1:
        step += 1
        number = algorithm(number)

    return step
