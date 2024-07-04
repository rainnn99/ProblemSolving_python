def solution(n):
    answer = [1, 1]

    for _ in range(n-1):
        answer.append(answer[-1] + answer[-2])

    return answer[-1] % 1234567