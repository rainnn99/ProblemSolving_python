def solution(price, money, count):
    need_money = 0
    for i in range(1, count+1):
        need_money += price * i
    if money > need_money:
        return 0
    else:
        return need_money - money