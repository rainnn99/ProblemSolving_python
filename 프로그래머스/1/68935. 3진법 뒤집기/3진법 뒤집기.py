def solution(n):
    digit = []
    while n:
        digit.append(int(n % 3))
        n //= 3
    digit = ''.join(str(num) for num in digit)
    return int(digit, 3)