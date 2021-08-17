def square(number):
    if number > 64 or number <= 0:
        raise ValueError('Number must be between 1-64')
    return 1 * 2**(number-1)

def total():
    return sum(square(x) for x in range(1, 65))
