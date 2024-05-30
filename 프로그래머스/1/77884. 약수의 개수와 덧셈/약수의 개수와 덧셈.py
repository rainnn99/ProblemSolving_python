def div_len(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // 1)
    return len(divs)


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if div_len(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer