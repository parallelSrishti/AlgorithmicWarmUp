# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


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


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    return (fibonacci_number_again(n+2, 10) + 9) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
