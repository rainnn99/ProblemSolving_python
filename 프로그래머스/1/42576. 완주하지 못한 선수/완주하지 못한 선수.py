def solution(participant, completion):
    answer = ''
    part = {}
    comp = {}

    for name in participant:
        if name in part:
            part[name] += 1
        else:
            part[name] = 1
    for name in completion:
        if name in comp:
            comp[name] += 1
        else:
            comp[name] = 1

    for name in part:
        if name not in comp or part[name] != comp[name]:
            answer = name
    return answer
