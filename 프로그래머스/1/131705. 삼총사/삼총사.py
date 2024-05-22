def solution(number):
    answer = 0
    idx = len(number)
    for i in range(idx):
        for j in range(i+1, idx):
            for k in range(j+1, idx):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer