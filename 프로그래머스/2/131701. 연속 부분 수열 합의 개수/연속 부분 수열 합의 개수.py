def solution(elements):
    answer = set()
    elements_buf = elements * 2

    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            answer.add(sum(elements_buf[j:j+i]))

    return len(answer)