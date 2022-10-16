import sys


def compute_min_refills(distance, miles_tank, n,  stops):
    num_refills, current_refill = 0, 0
    stops.insert(0, current_refill)
    stops.append(distance)
    while current_refill <= n:
        last_refill = current_refill
        while current_refill <= n and stops[current_refill+1] - stops[last_refill] <= miles_tank:
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill <= n:
            num_refills += 1
    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, _, stops))
