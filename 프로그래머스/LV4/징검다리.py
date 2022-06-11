def solution(distance, rocks, n):
    answer = 0
    start= 0
    end = distance
    rocks.sort()
    
    while start <= end:
        mid = (start + end)//2
        rm_rock = 0
        pr_rock = 0
        
        for rock in rocks:
            if rock - pr_rock < mid:
                rm_rock += 1
            else:
                pr_rock = rock
            if rm_rock > n:
                break
        
        if rm_rock > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer