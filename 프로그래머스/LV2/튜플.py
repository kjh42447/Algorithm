def solution(s):
    answer = []
    aset = set()
    l = s[2:-2].split('},{')
    l.sort(key=len)
    for i in l:
        ls = list(map(int, i.split(',')))
        lset = set(ls)
        num = int(list(lset-aset)[0])
        answer.append(num)
        aset = lset
    return answer