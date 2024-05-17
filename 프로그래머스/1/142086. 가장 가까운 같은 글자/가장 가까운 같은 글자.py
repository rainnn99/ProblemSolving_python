def solution(s):
    answer = []
    dict = {}
    for index, spell in enumerate(s):
        if spell not in dict:
            dict[spell] = index
            answer.append(-1)
        else:
            answer.append(index - dict[spell])
            dict[spell] = index
    return answer