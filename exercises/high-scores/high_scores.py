def latest(scores):
    return scores[len(scores) - 1]

def personal_best(scores):
    temp = scores
    temp.sort(reverse=True)
    return temp[0]

def personal_top_three(scores):
    temp = scores
    temp.sort(reverse=True)

    if len(scores) < 3:
        return temp
    else:
        return [temp[0], temp[1], temp[2]]
