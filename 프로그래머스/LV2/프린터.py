def solution(priorities, location):
    answer = 0
    length = len(priorities)
    q = [0 for i in range(9)]
    
    for priority in priorities:
        q[priority-1] += 1
    
    i = 8
    j = 0
    
    while(True):
        while q[i]:
            if i+1 == priorities[j]:
                answer += 1
                q[i] -= 1
                if j == location:
                    return answer
            j += 1
            j %= length
        i -= 1