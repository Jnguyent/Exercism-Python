def distance(strand_a, strand_b):
    # Raise value error if strands are not equal
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands are not equal length')

    # Sum() will count the number of Trues, len() would not work as it would count Falses and Trues
    return sum([x != y for (x, y) in zip(strand_a, strand_b)])
