def solution(s):
    buf = s.split(' ')
    buf = list(map(int, buf))
    answer = f'{str(min(buf))} {str(max(buf))}'
    return answer