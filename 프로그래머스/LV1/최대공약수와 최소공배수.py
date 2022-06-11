def solution(n, m):
    answer = [GCD(n, m), LCM(n, m)]
    return answer

def GCD(n, m):
    while m:
        n, m = m, n%m
    return n

def LCM(n, m):
    return n*m/GCD(n,m)