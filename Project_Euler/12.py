from math import *

def divisors(n):
    count = 1
    i = 2
    while i <= isqrt(n):
        power = 0
        while n % i == 0:
            n //= i
            power += 1
        count *= (power + 1)
        i += 1
    if n > 1:
        count *= 2
    return count

def solve():
    n = 1
    while True:
        if n % 2 == 0:
            a = n // 2
            b = n + 1
        else:
            a = n
            b = (n + 1) // 2
        total_divisors = divisors(a) * divisors(b)
        if total_divisors > 500:
            print(n * (n + 1) // 2)
            return
        n += 1

if __name__ == "__main__":
    solve()
