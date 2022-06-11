def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cur_num = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == s1[i%5]:
            cur_num[0] = cur_num[0] + 1
        if answers[i] == s2[i%8]:
            cur_num[1] = cur_num[1] + 1
        if answers[i] == s3[i%10]:
            cur_num[2] = cur_num[2] + 1
    max_num = max(cur_num)
    for i in range(3):
        if cur_num[i] == max_num:
            answer.append(i+1)
    return answer