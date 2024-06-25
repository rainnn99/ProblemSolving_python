def solution(s):
    answer = ''
    buf = s.split(' ')
    for i in buf:
        if i:
            i = i.upper()
            i = i[0] + i[1:].lower()
            answer += f'{i} '
        else:
            answer += ' '
    return answer[:len(answer)-1]