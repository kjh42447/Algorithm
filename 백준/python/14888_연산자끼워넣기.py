from sys import stdin

N = int(stdin.readline())
numList = list(map(int, stdin.readline().strip().split(' ')))
opList = list(map(int, stdin.readline().split(' ')))

minNum = 1000000000
maxNum = -1000000000

def calculate(sum, numIndex):
    global minNum, maxNum
    if numIndex >= N:
        if minNum > sum:
            minNum = sum
        if maxNum < sum:
            maxNum = sum
        return

    for i in range(4):
        if opList[i] != 0:
            newSum = operation(sum, numList[numIndex], i)
            opList[i] -= 1
            calculate(newSum, numIndex+1)
            opList[i] += 1

def operation(sum, num, i):
    if i == 0:
        return sum + num
    elif i == 1:
        return sum - num
    elif i == 2:
        return sum * num
    else:
        return int(sum/num)

calculate(numList[0], 1)
print(maxNum)
print(minNum)