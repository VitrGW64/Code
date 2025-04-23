from math import *
import time

dp = [[0] * 201 for _ in range(8)]  

def solve():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200

    for i in range(len(coins)):
        dp[i][0] = 1

    for i in range(len(coins)):
        for j in range(1, target + 1):
            if i > 0: dp[i][j] = dp[i - 1][j]
            else: dp[i][j] = 0

            if j >= coins[i]:
                dp[i][j] += dp[i][j - coins[i]]

    print(dp[len(coins) - 1][target]) 

if __name__ == "__main__":
    start_time = time.time()
    solve()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.4f} seconds")
