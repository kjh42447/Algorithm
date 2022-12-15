from sys import stdin

N = int(stdin.readline())
signList = list(stdin.readline().strip().split(' '))
numList = [-1 for i in range(10)]
curList = list()
count = 0

print(signList)

def isCorrect(num1, num2, sign):
    if sign == '<':
        return num1 < num2
    else:
        return num1 > num2

def func(idx):
    if count >= N-1:
        print(curList)
        return
    for i in range(9, -1, -1):
        if numList[i] == -1:
