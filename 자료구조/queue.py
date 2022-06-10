from collections import deque
import queue

#list로 push, pop 구현 가능
listQueue = list()
listQueue.append(1)
listQueue.append(2)
listQueue.pop()

#collections.deque 사용(이후 dequeue도 활용 가능)
dq = deque([])
dq.append(1)
dq.append(2)
dq.popleft()

#queue 모듈 사용
q = queue.Queue()
q.put(1)
q.put(2)
q.get()

