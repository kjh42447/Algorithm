import heapq

def solution(jobs):
    answer = 0
    t = 0
    joblen = len(jobs)
    hq = []
    jobs.sort()
    
    for _ in range(joblen):
        if not hq:
            if t < jobs[0][0]:
                t = jobs[0][0]
                
        if len(jobs) != 0:        
            while jobs[0][0] <= t:
                heapq.heappush(hq, jobs.pop(0)[::-1])
                if len(jobs) == 0:
                    break
            
        nowtask = heapq.heappop(hq)
        t += nowtask[0]
        answer += t - nowtask[1]

    return int(answer/joblen)