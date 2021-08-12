days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
     'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

verses = [
    'a Partridge in a Pear Tree.',
    'two Turtle Doves, and ',
    'three French Hens, ',
    'four Calling Birds, ',
    'five Gold Rings, ',
    'six Geese-a-Laying, ',
    'seven Swans-a-Swimming, ',
    'eight Maids-a-Milking, ',
    'nine Ladies Dancing, ',
    'ten Lords-a-Leaping, ',
    'eleven Pipers Piping, ',
    'twelve Drummers Drumming, '
]

def recite(start_verse, end_verse):
    return [verse(n) for n in range(start_verse, end_verse + 1)]

def verse(n):
    return(f'On the {days[n-1]} day of Christmas my true love gave to me: '
        f"{''.join(verses[n-1::-1])}"
        )


recite(3, 3)