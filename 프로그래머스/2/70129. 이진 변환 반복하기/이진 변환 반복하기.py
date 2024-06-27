def solution(s):
    del_0, i = 0, 0
    while s != '1':
        del_buf = s.count('0')
        print(s)
        s = bin(len(s) - del_buf)[2:]
        del_0 += del_buf
        i += 1

    return [i, del_0]