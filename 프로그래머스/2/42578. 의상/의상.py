from collections import defaultdict


def solution(clothes):
    sort_c = defaultdict(int)

    for item in clothes:
        key = item[1]
        sort_c[key] += 1

    clothes = list(sort_c.values())

    answer = 1
    for count in sort_c.values():
        answer *= (count + 1)

    return answer - 1