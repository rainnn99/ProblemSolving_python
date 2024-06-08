def solution(n, arr1, arr2):
    answer = []

    for first, second in zip(arr1, arr2):
        buf = ''
        first = format(first, f'0{n}b')
        second = format(second, f'0{n}b')
        for j in range(n):
            if first[j] == '0' and second[j] == '0':
                buf += ' '
            else:
                buf += '#'
        answer.append(buf)
    return answer