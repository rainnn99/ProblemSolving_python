def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    corrects = [0, 0, 0]

    for idx, correct in enumerate(answers):
        if correct == first[idx % 5]:
            corrects[0] += 1
        if correct == second[idx % 8]:
            corrects[1] += 1
        if correct == third[idx % 10]:
            corrects[2] += 1

    buf = max(corrects)
    for idx, i in enumerate(corrects):
        if i == buf:
            answer.append(idx + 1)

    return answer