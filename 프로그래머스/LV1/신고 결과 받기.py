def solution(id_list, report, k):
    n = len(id_list)
    answer = [0 for i in range(n)]

    check = [[0]*n for i in range(n)]
    reported = []
    name = {}
    a = 0

    for id in id_list:
        name[id] = a
        a = a+1

    for i in report:
        report_detail = i.split()
        if check[name[report_detail[1]]][name[report_detail[0]]] == 0:
            check[name[report_detail[1]]][name[report_detail[0]]] = 1

    for i in range(n):
        if sum(check[i]) >= k:
            reported.append(1)
        else:
            reported.append(0)

    for i in range(n):
        for j in range(n):
            if check[i][j] == 1 and reported[i]:
                answer[j] = answer[j] + 1

    return answer