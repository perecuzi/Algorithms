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


a = int(input())
print(l_d_fibo_sum(a))



