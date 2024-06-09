def solution(x, n):
    answer = [x]
    for i in range(1, n):
        answer.append(x+i*x)
    return answer