def calc_fib(n):
    fibonacci = [0] * (n+1)
    fibonacci[0] = 0
    fibonacci[1] = 1
    for i in range(2, n+1):
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    return fibonacci


def last_digit_of_fibo_sum_of_squares(n):
    f = [0] * 61
    f = calc_fib(60)
    ss = (f[n % 60] % 10) * (f[(n + 1) % 60] % 10)
    return ss % 10


a = int(input())
print(last_digit_of_fibo_sum_of_squares(a))


