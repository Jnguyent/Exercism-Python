def slices(series, length):
    if length > len(series):
        raise ValueError('length is too large')
    if length == 0:
        raise ValueError('length cannot be zero')
    if length < 0:
        raise ValueError('length cannot be negative')
    if len(series) == 0:
        raise ValueError('empty series is invalid')

    pass
