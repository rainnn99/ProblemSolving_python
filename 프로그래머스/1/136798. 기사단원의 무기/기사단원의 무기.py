def count_div(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count


def solution(number, limit, power):
    answer = 0
    iron_buf = []
    for i in range(1, number + 1):
        iron_buf.append(count_div(i))
    for iron in iron_buf:
        if iron > limit:
            answer += power
        else:
            answer += iron
    return answer