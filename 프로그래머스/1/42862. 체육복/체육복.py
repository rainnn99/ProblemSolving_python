def solution(n, lost, reserve):
    stats = {key: 1 for key in range(1, n+1)}
    for student in lost:
        stats[student] = 0
    for student in reserve:
        stats[student] += 1

    new_lost = {key: 0 for key, value in stats.items() if value == 0}
    new_reserve = {key: 2 for key, value in stats.items() if value == 2}

    for borrow in new_lost:
        if borrow - 1 in new_reserve:
            new_lost[borrow] += 1
            new_reserve.pop(borrow - 1)
        elif borrow + 1 in new_reserve:
            new_lost[borrow] += 1
            new_reserve.pop(borrow + 1)

    final_lost = [key for key, value in new_lost.items() if value == 0]
    answer = n - len(final_lost)
    return answer