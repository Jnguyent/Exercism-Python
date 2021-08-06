# This function reverses a number
def reverse(number):
    return int(str(number)[::-1])

def largest(min_factor, max_factor):
    # Raise value error if min > max
    if min_factor > max_factor:
        raise ValueError('Min factor is more than max factor')

    # Create a list of palindrome products from min to max
    palindrome_list = [x*y for x in range(min_factor, max_factor + 1) for y in range(min_factor, max_factor + 1) if x*y == reverse(x*y)]

    # Error if palindromes are empty
    if len(palindrome_list) > 0:
        # Get max value
        value = max(palindrome_list)
    else:
        value = None

    # Get the factors associated with the palindrome value
    factors_list = [(x,y) for x in range(min_factor, max_factor + 1) for y in range(min_factor, max_factor + 1) if x*y == value and x <= y]
    return value, factors_list


def smallest(min_factor, max_factor):
    # Raise value error if min > max
    if min_factor > max_factor:
        raise ValueError('Min factor is more than max factor')

    # Create a list of palindrome products from min to max
    palindrome_list = [x*y for x in range(min_factor, max_factor + 1) for y in range(min_factor, max_factor + 1) if x*y == reverse(x*y)]

    # Error if palindromes are empty
    if len(palindrome_list) > 0:
        # Get min value
        value = min(palindrome_list)
    else:
        value = None

    # Get the factors associated with the palindrome value
    factors_list = [(x,y) for x in range(min_factor, max_factor + 1) for y in range(min_factor, max_factor + 1) if x*y == value and x <= y]
    return value, factors_list
