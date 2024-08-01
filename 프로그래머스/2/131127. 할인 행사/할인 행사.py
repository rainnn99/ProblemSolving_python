from collections import Counter


def solution(want, number, discount):
    answer = 0
    ww = {key:value for key, value in zip(want, number)}

    for i in range(len(discount) - 9):
        count = Counter(discount[i:i+10])
        if ww == count:
            answer += 1
            
    return answer