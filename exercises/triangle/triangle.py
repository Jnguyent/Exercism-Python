def inequality(sides):
    max_side = max(sides)
    two_sides = sum(sides) - max_side

    return max_side <= two_sides

def equilateral(sides):
    for x in sides:
        if x == 0:
            return False
    return len(set(sides)) == 1


def isosceles(sides):
    return ((len(set(sides)) == 1 or len(set(sides)) == 2) and inequality(sides))

def scalene(sides):
    return len(set(sides)) == 3 and inequality(sides)
