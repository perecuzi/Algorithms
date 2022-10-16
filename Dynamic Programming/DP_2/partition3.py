# Uses python3
import sys


def subsetSum(S, n, a, b, c):
    if a == 0 and b == 0 and c == 0:
        return True
    if n < 0:
        return False
    A = False
    if a - S[n] >= 0:
        A = subsetSum(S, n - 1, a - S[n], b, c)
    B = False
    if not A and (b - S[n] >= 0):
        B = subsetSum(S, n - 1, a, b - S[n], c)
    C = False
    if (not A and not B) and (c - S[n] >= 0):
        C = subsetSum(S, n - 1, a, b, c - S[n])
    return A or B or C


def partition3(A):
    if len(A) < 3:
        return 0
    total = sum(A)
    if (sum(A) % 3) == 0 and subsetSum(A, len(A) - 1, total // 3, total // 3, total // 3):
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

