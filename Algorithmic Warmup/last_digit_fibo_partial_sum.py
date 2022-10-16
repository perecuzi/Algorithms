def l_d_fibo_sum(n):
    fibonacci = [0] * 2
    fibonacci[0] = 0
    fibonacci[1] = 1
    if n > 1:
        rem = n % 60
        if rem == 0:
            return 0
        for i in range(2, rem + 3):
            f = (fibonacci[0] + fibonacci[1]) % 60
            fibonacci[0] = fibonacci[1]
            fibonacci[1] = f
        return (fibonacci[1] - 1) % 10
    elif n == 1:
        return 1
    else:
        return 0




def l_d_fibo_partial_sum(m, n):
    p_sum = l_d_fibo_sum(n) - l_d_fibo_sum(m - 1)
    return p_sum % 10


a, b = map(int, input().split())
print(l_d_fibo_partial_sum(a, b))



