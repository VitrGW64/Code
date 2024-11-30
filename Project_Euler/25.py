from math import ceil, sqrt, log10

def solve():
    return ceil((1000 - 1 + log10(sqrt(5))) / log10((1 + sqrt(5)) / 2))

if __name__ == '__main__':
    print(solve())
