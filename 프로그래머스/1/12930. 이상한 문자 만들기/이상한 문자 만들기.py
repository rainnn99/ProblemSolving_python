def solution(s):
    answer = ''
    buf = s.split(" ")

    for word in buf:
        for idx, value in enumerate(word):
            if idx % 2 == 0:
                answer += value.upper()
            else:
                answer += value.lower()
        answer += ' '

    return answer[:len(answer)-1]