from collections import Counter


def solution(k, tangerine):
    answer = 0
    buf = 0
    tangerine_dict = dict(Counter(tangerine))
    sort_dict = dict(sorted(tangerine_dict.items(), key=lambda item: item[1], reverse=True))

    for number in sort_dict.values():
        buf += number
        answer += 1
        if buf >= k:
            break
    return answer