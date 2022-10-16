# Uses python3
import sys


def optimal_sequence(n):
    count_h = [0] * (n + 1)
    count_h[1] = 1
    for i in range(2, n + 1):
        ind = [i - 1]
        if i % 2 == 0:
            ind.append(i // 2)
        if i % 3 == 0:
            ind.append(i // 3)
        min_h = min([count_h[x] for x in ind])
        count_h[i] = min_h + 1
    ptr = n
    optimal_seq = [ptr]
    while ptr != 1:
        cand = [ptr - 1]
        if ptr % 2 == 0:
            cand.append(ptr // 2)
        if ptr % 3 == 0:
            cand.append(ptr // 3)
        ptr = min(
            [(c, count_h[c]) for c in cand],
            key=lambda x: x[1]
        )[0]
        optimal_seq.append(ptr)
    return reversed(optimal_seq)


n = int(sys.stdin.read())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=" ")
