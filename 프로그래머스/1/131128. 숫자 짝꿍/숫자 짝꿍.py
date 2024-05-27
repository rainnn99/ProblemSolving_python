from collections import defaultdict


def solution(X, Y):
    answer = ''
    x_dict = defaultdict(int)
    y_dict = defaultdict(int)

    for i in str(X):
        x_dict[i] += 1
    for i in str(Y):
        y_dict[i] += 1

    for i in sorted(x_dict.keys(), key=int, reverse=True):
        if str(i) in y_dict:
            answer += str(i) * min(x_dict[str(i)], y_dict[str(i)])

    if not answer:
        return '-1'
    
    if len(answer) == answer.count('0'):
        return '0'
    
    return answer