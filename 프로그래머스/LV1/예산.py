def solution(d, budget):
    sumd = 0
    i = 0
    d.sort()
    for i, value in enumerate(d):
        if sumd + value > budget:
            return i
        sumd += value 
    return i+1