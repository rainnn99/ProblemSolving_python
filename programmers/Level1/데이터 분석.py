#https://school.programmers.co.kr/learn/courses/30/lessons/250121 [PCCE 기출문제] 10번 / 데이터 분석

def solution(data, ext, val_ext, sort_by):
    data_type = {"code" : 0, "date" : 1, "maximum" : 2, "remain": 3}
    select = [d for d in data if d[data_type[ext]]<val_ext]
    answer = sorted(select, key = lambda x : x[data_type[sort_by]])
    return answer
