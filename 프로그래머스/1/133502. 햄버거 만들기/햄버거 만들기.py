def solution(ingredient):
    answer = 0
    hamburger = []
    for i in ingredient:
        hamburger.append(i)
        if hamburger[-4:] == [1, 2, 3, 1]:
            answer += 1
            del hamburger[-4:]
    return answer