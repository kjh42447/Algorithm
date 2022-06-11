import heapq

def solution(scoville, K):
    heap = []
    answer = 0
    for i in scoville:
        heapq.heappush(heap, i)
    while heap[0] < K:
        if len(heap) < 2:
            answer = -1
            break
        else:
            f1 = heapq.heappop(heap)
            f2 = heapq.heappop(heap)
            heapq.heappush(heap, f1 + f2*2)
            answer = answer + 1
    return answer