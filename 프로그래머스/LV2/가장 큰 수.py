def solution(numbers):
    answer = ''
    numstring = []
    for number in numbers:
        numstr = str(number)*3
        numstring.append(numstr)

    numstring.sort(reverse=True)

    for numstr in numstring:
        l = len(numstr)//3
        answer = answer + numstr[:l]

    return str(int(answer))