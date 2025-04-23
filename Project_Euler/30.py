from math import *

def solve():
    nums = []
    for i in range(1111, 199999):
        digit_sum = 0
        n = i
        while(n):
            digit_sum += (n % 10) ** 5
            n //= 10
        if digit_sum == i:
            nums.append(i)
    
    print(sum(nums))

if __name__ == "__main__":
    solve()