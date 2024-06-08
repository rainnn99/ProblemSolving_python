from itertools import combinations


def solution(nums):
    answer = 0

    is_prime = [True] * 3001
    p = 2
    while p * p <= 3000:
        if is_prime[p]:
            for i in range(p * p, 3001, p):
                is_prime[i] = False
        p += 1

    prime = {}
    for p in range(2, 3001):
        if is_prime[p]:
            prime[p] = 0

    for result in combinations(nums, 3):
        if sum(result) in prime:
            answer += 1

    return answer