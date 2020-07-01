from itertools import combinations


def place_ones(size, count):
    for positions in combinations(range(size), count):
        p = [0] * size

        for i in positions:
            p[i] = 1

        yield p

p = list(place_ones(6,3))
print(p)