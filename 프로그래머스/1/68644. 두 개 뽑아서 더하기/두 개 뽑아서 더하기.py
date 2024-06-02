def solution(numbers):
    answer = []
    for idx, i in enumerate(numbers):
        for j in numbers[idx+1:]:
            answer.append(i+j)
    answer = set(answer)
    answer = sorted(answer)
    return answer