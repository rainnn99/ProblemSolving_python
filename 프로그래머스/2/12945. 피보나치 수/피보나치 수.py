def solution(n):
    buf = [0, 1]
    for i in range(2, n+1):
        buf.append(buf[i-2] + buf[i-1])
    return buf[-1] % 1234567