def solution(survey, choices):
    answer = ''
    mbti = ['RT', 'CF', 'JM', 'AN']
    result = [0, 0, 0, 0]

    for s, c in zip(survey, choices):
        c -= 4
        if s in mbti:
            result[mbti.index(s)] += (-1 * c)
        else:
            result[mbti.index(s[::-1])] += c

    for i in range(len(mbti)):
        if result[i] > 0 or result[i] == 0:
            answer += mbti[i][0]
        else:
            answer += mbti[i][1]
    return answer