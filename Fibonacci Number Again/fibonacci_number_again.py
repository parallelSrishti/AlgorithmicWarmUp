# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number(n):
    fib = [0, 1]
    for i in range(n + 1):
        if i > 1:
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    i = 2
    while i < m * m:
        if fibonacci_number(i) % m == 0 and fibonacci_number(i + 1) % m == 1:
            break
        else:
            i += 1
    n %= i
    return fibonacci_number(n) % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
