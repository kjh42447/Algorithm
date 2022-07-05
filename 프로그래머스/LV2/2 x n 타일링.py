def solution(n):
    answer = [1,1]
    for i in range(2,n+1):
        answer[i%2] += answer[(i+1)%2]
    return int(answer[n%2]%1000000007)