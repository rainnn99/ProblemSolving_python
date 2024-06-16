def solution(a, b):
    w = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_buf = 0

    for i in range(a-1):
        day_buf += day[i]
    day_buf += b

    return w[day_buf % 7]