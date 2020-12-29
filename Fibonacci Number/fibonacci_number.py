# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    fib = [0, 1]
    for i in range(n+1):
        if i > 1:
            fib.append(fib[i-1] + fib[i-2])
    return fib[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
