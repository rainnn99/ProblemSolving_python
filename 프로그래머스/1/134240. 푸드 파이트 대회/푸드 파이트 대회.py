def solution(food):
    answer = ''
    for food_name, number in enumerate(food):
        if int(number) >= 2:
            for _ in range(int(number)//2):
                answer += str(food_name)
    answer = answer + '0' + answer[::-1]
    return answer