N = 1234567891011


def math_1(n: int = N):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    print(count)


math_1()
