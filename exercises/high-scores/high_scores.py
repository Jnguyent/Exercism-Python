def latest(scores):
    return scores[len(scores) - 1]

def personal_best(scores):
    scores.sort(reverse=True)
    return scores[0]

def personal_top_three(scores):
    scores.sort(reverse=True)

    if len(scores) < 3:
        return scores
    else:
        return [scores[0], scores[1], scores[2]]

