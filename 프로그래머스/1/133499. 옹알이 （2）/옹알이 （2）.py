def solution(babbling):
    answer = 0
    bab = {"aya", "ye", "woo", "ma"}
    for call in babbling:
        for j in bab:
            if j * 2 not in call:
                call = call.replace(j, ' ')
        if call.isspace():
            answer += 1
    return answer