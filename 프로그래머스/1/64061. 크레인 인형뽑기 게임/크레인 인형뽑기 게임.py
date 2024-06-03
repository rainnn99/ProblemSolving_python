def find_doll(arr):
    for index, value in enumerate(arr):
        if value != 0:
            return value, index
    return None, -1


def solution(board, moves):
    answer = 0
    board_matrix = [list(row) for row in zip(*board)]
    basket = []
    for i in moves:
        value, index = find_doll(board_matrix[i-1])
        if index >= 0:
            basket.append(value)
            board_matrix[i-1][index] = 0
        try:
            if basket[-1] == basket[-2]:
                answer += 2
                del basket[-2:]
        except IndexError:
            pass
    return answer