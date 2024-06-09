def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        buf = []
        for j in range(len(arr1[i])):
            buf1 = 0
            buf1 = arr1[i][j] + arr2[i][j]
            buf.append(buf1)
        answer.append(buf)
    return answer