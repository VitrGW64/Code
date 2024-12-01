def solve():
    n = 2 ** 1000
    sum = 0

    while n > 0:
        sum = sum + (n % 10)
        n = n // 10
    
    return sum

if __name__ == '__main__':
    print(solve())