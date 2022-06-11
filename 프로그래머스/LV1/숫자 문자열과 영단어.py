import re

def solution(s):
    li = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        s = re.sub(li[i], str(i), s)
    answer = int(s)
    return answer