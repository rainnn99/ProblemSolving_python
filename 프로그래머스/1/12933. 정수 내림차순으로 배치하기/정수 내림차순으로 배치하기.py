from collections import Counter


def solution(n):
    answer = ''
    count = dict(Counter(str(n)))
    sorted_count = sorted(count.keys(), reverse=True)

    for key in sorted_count:
        answer += key * count[key]
    return int(answer)