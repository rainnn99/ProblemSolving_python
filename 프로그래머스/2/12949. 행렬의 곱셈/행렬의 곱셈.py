def solution(arr1, arr2):
    x, y, z = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0 for _ in range(z)] for _ in range(x)]

    for i in range(x):
        for j in range(z):
            for k in range(y):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer