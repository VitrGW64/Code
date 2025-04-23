from math import *
import time
import psutil
import os

def solve():
    sieve = [True] * 1000000
    primes = []
    visited = [False] * 1000000
    MAXN = 1000000
    cnt = 0

    sieve[0] = sieve[1] = False
    for i in range(2, MAXN):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, MAXN, i):
                sieve[j] = False

    for prime in primes:
        if visited[prime]: continue

        s = str(prime)
        rotations = []
        circular = True

        for i in range(len(s)):
            rotation = int(s[i:] + s[:i])
            rotations.append(rotation)

            if not sieve[rotation]:
                circular = False
                break

        if circular:
            for num in rotations:
                visited[num] = True
            cnt += len(set(rotations))  

    print(cnt)

if __name__ == "__main__":
    start_time = time.time()
    solve()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.4f} seconds")
    process = psutil.Process(os.getpid())
    memory_usage_mb = process.memory_info().rss / (1024 ** 2)
    print(f"Memory usage: {memory_usage_mb:.2f} MB")