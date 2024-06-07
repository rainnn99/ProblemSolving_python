import re


def solution(dartResult):
    answer = 0
    result_buf = []

    pattern = r"(\d+)([SDT])([^\d])*"
    matches = re.findall(pattern, dartResult)

    for match in matches:
        score, bonus, price = match
        score = int(score)

        if bonus == 'S':
            score = score
        elif bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3

        result_buf.append([score, price])

    for i in range(len(result_buf)):
        score, price = result_buf[i]

        if price == '*':
            result_buf[i][0] = score * 2
            if i > 0:
                result_buf[i - 1][0] *= 2
        elif price == '#':
            result_buf[i][0] = score * -1

    answer = sum([score for score, _ in result_buf])
    return answer