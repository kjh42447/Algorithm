def solution(s):
    i = 0
    j = len(s)
    
    if j%2 == 1:
        return 0
    
    s = list(s)
    
    for _ in range(j*j):
        if i+1 >= j:
            break
        if s[i] == s[i+1]:
            del s[i]
            del s[i]
            i = -1
            j -= 2
        i+= 1
    
    if s:
        return 0
    else:
        return 1