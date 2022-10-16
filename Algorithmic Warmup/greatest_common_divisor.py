def gcd(ax, bx):
    while bx > 0:
        ay = bx
        by = ax % bx
        ax = ay
        bx = by
    current_gcd = ax

    return current_gcd

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
