def solution(lottos, win_nums):
    result = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer = []
    rank = 0

    for i in lottos:
        if i in win_nums:
            rank += 1
    missing = lottos.count(0)

    answer.append(result[rank+missing])
    answer.append(result[rank])

    return answer