import sys

INF = 100000


def coin_change(d, n):
    k = len(d)-1
    M = [0] * (n + 1)
    for j in range(1, n + 1):
        minimum = INF
        for i in range(1, k + 1):
            if j >= d[i]:
                minimum = min(minimum, 1 + M[j - d[i]])
        M[j] = minimum
    return M[n]


if __name__ == '__main__':
    coins = [0, 1, 3, 4]
    m = int(sys.stdin.read())
    print(coin_change(coins, m))
