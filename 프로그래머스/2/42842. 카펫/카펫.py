def solution(brown, yellow):
    tile = brown + yellow
    pairs = []

    for i in range(1, int(tile ** 0.5) + 1):
        if tile % i == 0:
            pairs.append((i, tile // i))

    for i in pairs:
        if (i[0] - 2) * (i[1] - 2) == yellow:
            return sorted(i, reverse=True)