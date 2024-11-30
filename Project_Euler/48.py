MOD = 10**10  

def modexp(a, b, mod):
    result = 1
    a %= mod
    while b > 0:
        if b % 2 == 1: 
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result

def solve():
    total = 0
    for i in range(1, 1001):
        total = (total + modexp(i, i, MOD)) % MOD
    return total

if __name__ == "__main__":
    print(solve())  # Output: The last 10 digits
