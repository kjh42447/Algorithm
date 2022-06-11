def solution(progresses, speeds):
    answer = []
    
    p = progresses
    s = speeds

    while p:
        count = 0
        for i in range(len(p)):
            p[i] = p[i] + s[i]
        
        while p[0] >= 100:
            p.pop(0)
            s.pop(0)
            count = count+1
            if not p:
                break
        
        if count:
            answer.append(count)
    
    return answer