def solution(lottos, win_nums):
    answer = [7, 7]

    for i in lottos:
        if i in win_nums:
            answer[0] = answer[0]-1
            answer[1] = answer[1]-1
        elif i == 0:
            answer[0] = answer[0]-1

    if answer[0] == 7:
        answer[0] = 6
    if answer[1] == 7:
        answer[1] = 6

    return answer