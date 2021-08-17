def factors(value):
    prime_factors = []
    factor = 2
    while value > 1:
        if value % factor == 0:
            prime_factors.append(factor)
            value /= factor
        else:
            if factor > 2:
                factor += 2
            else:
                factor += 1
    return prime_factors
