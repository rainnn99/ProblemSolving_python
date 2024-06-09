def solution(x):
    str_x = str(x)
    buf = 0
    for i in str_x:
        buf += int(i)

    if x % buf == 0:
        return True
    else:
        return False