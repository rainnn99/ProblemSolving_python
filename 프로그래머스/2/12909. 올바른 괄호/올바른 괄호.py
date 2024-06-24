def solution(s):
    buf = [s[0]]
    if buf[0] == ')':
        return False

    s = s[1:]
    for letter in s:
        if letter == '(':
            buf.append(letter)
        elif not buf:
            return False
        else:
            buf.pop()

    if buf:
        return False
    else:
        return True