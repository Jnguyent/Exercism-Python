def is_valid(isbn):

    # If length of isbn is 0
    if len(isbn) == 0:
        return False

    # Make a string for testing that removes all nondigits (excluding checking number)
    temp = ''.join(x for x in isbn[:-1] if x.isdigit())
    # Add checking number
    temp += isbn[-1]

    # Check for valid ISBN length
    if len(temp) != 10:
        return False
    # Check for valid checking number
    if isbn[-1] != 'X' and not isbn[-1].isdigit():
        return False

    # Evaluation ISBN formula
    total = 0
    for i in range(9):
        total += int(temp[i]) * (10 - i)

    if temp[-1] == 'X':
        total += 10
    else:
        total += int(temp[-1])

    return total % 11 == 0
