from math import *
import time

dp = {}

def d(n):
    if n in dp:
        return dp[n]
    
    sum = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            if i != n // i and n // i != n:
                sum += n // i
    
    dp[n] = sum
    return sum


def solve():
    nums = []
    for i in range(1, 10000):
        a = d(i)
        b = d(a)
        if b == i and a != b:
            nums.append(i)

    print(sum(nums))

if __name__ == "__main__":
    start_time = time.time()
    solve()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.4f} seconds")