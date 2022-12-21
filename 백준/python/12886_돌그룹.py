from sys import stdin
from collections import deque

def bfs(root):
    sumNum = sum(root)
    visited = [[False] *(sumNum+1) for i in range(sumNum+1)]
    queue = deque([root])

    while queue:
        n = queue.popleft()
        
        if n[0] == n[1] & n[0] == n[2]:
            return 1
        
        for i in range(3):
            newN = list()
            if n[i%3] == n[(i+1)%3]:
                continue
            elif n[i%3] > n[(i+1)%3]:
                newN.append(n[i%3]-n[(i+1)%3])
                newN.append(2*n[(i+1)%3])
                newN.append(n[(i+2)%3])
                newN.sort()
            else:
                newN.append(n[i%3]*2)
                newN.append(n[(i+1)%3]-n[i%3])
                newN.append(n[(i+2)%3])
                newN.sort()
            if not visited[min(newN)][max(newN)]:
                queue.append(newN)
                visited[min(newN)][max(newN)] = True 
    
    return 0
            

numList = list(map(int, stdin.readline().strip().split(' ')))

if sum(numList) % 3 != 0:
    print(0)
else:
    print(bfs(numList))
