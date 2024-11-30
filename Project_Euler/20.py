def factorial(n):
    curr = 1
    for i in range(2, n + 1):
        curr = curr * i
    
    return curr

def solve():
    fact = factorial(100)
    sum = 0
    while fact > 0:
        sum = sum + (fact % 10)
        fact = fact // 10
    
    return sum

if __name__ == '__main__':
    print(solve())