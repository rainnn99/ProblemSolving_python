def solution(n):
    buf = []
    n -= 1
    for i in range(1, int(n**0.5 + 1)):
        if n % i == 0:
            buf.append(i)
            if i != n // i:
                buf.append(n // i)
    buf.sort()
    return buf[1]