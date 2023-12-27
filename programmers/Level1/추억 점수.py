#https://school.programmers.co.kr/learn/courses/30/lessons/176963 추억 점수

def solution(name, yearning, photo):
    answer = []
    score = {name : yearing for name, yearing in zip(name, yearning)}
    for rows in photo:
        buf = 0
        for val in rows:
            if val in score:
                buf += score[val]
        answer.append(buf)
    return answer