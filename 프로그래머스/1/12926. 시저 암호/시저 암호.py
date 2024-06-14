def solution(s, n):
    answer = ''
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for case in s:
        if case == ' ':
            answer += ' '
        elif case in lower_case:
            buf = lower_case.index(case) + n
            if buf >= 26:
                buf -= 26
            answer += lower_case[buf]
        else:
            buf = upper_case.index(case) + n
            if buf >= 26:
                buf -= 26
            answer += upper_case[buf]
    return answer