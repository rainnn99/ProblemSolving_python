import math


def solution(n, a, b):
    for i in range(1, int(math.log2(n)) + 1):
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        if a == b:
            return i