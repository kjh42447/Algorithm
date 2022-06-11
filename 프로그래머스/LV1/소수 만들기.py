import math

def solution(nums):
    answer = 0
    n = len(nums)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if is_prime_number(nums[i]+nums[j]+nums[k]):
                    answer += 1
    return answer

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True