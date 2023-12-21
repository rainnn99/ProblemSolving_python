#https://school.programmers.co.kr/learn/courses/30/lessons/178871 달리기 경주

def solution(players, callings):
    dict={player : index for index, player in enumerate(players)}
    for i in callings:
        call = dict[i]
        players[call-1], players[call] = players[call], players[call-1]
        buf = dict[i]
        dict[players[call-1]] = dict[players[call]]
        dict[players[call]] = buf
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))

# def solution(players, callings):
#     for i in callings:
#         call = players.index(i)
#         players[call-1], players[call] = players[call], players[call-1]