def solution(n):
    answer = 0
    for i in range(1, n+1):
        buf = 0
        for j in range(i, n+1):
            buf += j
            if buf == n:
                answer += 1
                break
            elif buf > n:
                break

    return answer