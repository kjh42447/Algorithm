from sys import stdin

def matrix_mult(A, B):
    temp = [[0] * (len(A)) for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                if A[i][j] * B[j][k]:
                    temp[i][k] = 1
    return temp


def matrix_pow(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        temp = matrix_pow(A, n//2)
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(A, n-1)
        return matrix_mult(temp, A)

N, K, M = map(int, stdin.readline().strip().split(' '))
matrix = [[False for i in range(N)] for j in range(N)]

for i in range(N):
    a, b = map(int, stdin.readline().strip().split(' '))
    matrix[i][a-1] = True
    matrix[i][b-1] = True

powMatrix = matrix_pow(matrix, K)

for i in range(M):
    start, target = map(int, stdin.readline().strip().split(' '))
    print("death" if powMatrix[start-1][target-1] else "life")

