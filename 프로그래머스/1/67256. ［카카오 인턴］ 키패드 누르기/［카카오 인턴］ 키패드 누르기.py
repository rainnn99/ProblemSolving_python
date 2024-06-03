def get_manhattan_distance(x, y):
    return abs(y[0] - x[0]) + abs(y[1] - x[1])


def solution(numbers, hand):
    answer = ''
    hand = hand[0].upper()
    hand_location = {'L': '*', 'R': '#'}
    num_location = {'1': [0, 0], '2': [0, 1], '3': [0, 2], '4': [1, 0], '5': [1, 1], '6': [1, 2], '7': [2, 0], '8': [2, 1], '9': [2, 2], '*': [3, 0], '0': [3, 1], '#': [3, 2]}
    click_left = ['1', '4', '7']
    click_right = ['3', '6', '9']

    for num in numbers:
        num_str = str(num)
        if num_str in click_left:
            answer += 'L'
            hand_location['L'] = num_str
        elif num_str in click_right:
            answer += 'R'
            hand_location['R'] = num_str
        else:
            left_distance = get_manhattan_distance(num_location[hand_location['L']], num_location[num_str])
            right_distance = get_manhattan_distance(num_location[hand_location['R']], num_location[num_str])
            if left_distance > right_distance:
                answer += 'R'
                hand_location['R'] = num_str
            elif left_distance < right_distance:
                answer += 'L'
                hand_location['L'] = num_str
            else:
                answer += hand
                hand_location[hand] = num_str

    return answer