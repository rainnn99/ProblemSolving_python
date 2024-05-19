def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)//m):
        buf = score[i*m:(i+1)*m]
        answer += buf[-1] * m
    return answer