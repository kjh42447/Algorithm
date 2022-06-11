def solution(lines):
    answer = 0
    log=[]
    for line in lines:
        d, s, t = line.split()
        s = s.split(':')
        t = float(t[:-1])
        end = int(s[0]) * 3600 + int(s[1]) * 60 + float(s[2])
        start = end - t + 0.001
        log.append([start, end])
    for i in range(len(lines)):
        count = 0
        cur_time = log[i][1]
        for j in range(i, len(lines)):
            if cur_time > log[j][0] - 1:
                count = count + 1
        answer = max(answer, count)
    return answer