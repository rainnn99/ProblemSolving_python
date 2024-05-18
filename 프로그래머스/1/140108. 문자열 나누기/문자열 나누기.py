def solution(s):
    answer = 0
    count_first, count_other = 0, 0
    for i in s:
        if count_other == count_first:
            answer += 1
            index = i
        if index == i:
            count_first += 1
        else:
            count_other += 1
    return answer

