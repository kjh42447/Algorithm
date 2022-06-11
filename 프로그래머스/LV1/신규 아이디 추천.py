import re

def solution(new_id):
    str1 = new_id.lower()
    str2 = re.sub(r"[^a-z0-9-_.]","", str1)
    str3 = re.sub('[.]+', '.', str2)
    str4 = str3
    if str4:
        if str4[0] == '.' :
            str4 = str4[1:]
    if str4:
        if str4[-1] == '.':
            str4 = str4[:-1]
    str5 = str4
    if not str5:
        str5 = 'a'
    str6 = str5
    if len(str6) > 15:
        str6 = str6[:15]
        if str6[-1] == '.':
            str6 = str6[:-1]
    str7 = str6
    while len(str7) < 3:
        str7 = str7 + str7[-1]
    answer = str7
    return answer