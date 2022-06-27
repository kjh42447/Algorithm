def solution(n):
    answer = 0
    tmp = ''

    while n != 0:
        tmp = tmp + str(n%3)
        n = int(n/3)

    ltmp = len(tmp)

    for i in range(ltmp):
        answer += int(tmp[ltmp-i-1])*3**i

    return answer