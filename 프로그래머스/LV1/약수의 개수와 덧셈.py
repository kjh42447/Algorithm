def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        sqrt = i ** (1/2)

        if sqrt % 1 == 0:
            answer -= i
        else:
            answer += i

    return answer