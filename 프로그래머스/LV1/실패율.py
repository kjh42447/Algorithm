def solution(N, stages):
    answer = []
    num = len(stages)
    st_list = [[i, 0] for i in range(1, N+2)]
    
    for stage in stages:
        st_list[stage-1][1] += 1
    
    st_list.pop()
    
    for i in range(N):
        if num != 0:
            tmp = st_list[i][1]
            st_list[i][1] /= num
            num -= tmp
        else:
            break
            
    st_list = sorted(st_list, key = lambda x : (-x[1], x[0]))
    
    for a in st_list:
        answer.append(a[0])
        
    return answer