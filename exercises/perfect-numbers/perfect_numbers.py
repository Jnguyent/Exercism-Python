def classify(number):
    if number <= 0:
        raise ValueError("Not a positive integer")

    total = 0

    for x in range(1, number):
        if number % x == 0:
            total += x

    if total == number:
        return "perfect"
    elif total > number:
        return "abundant"
    else:
        return "deficient"