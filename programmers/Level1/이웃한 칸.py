#https://school.programmers.co.kr/learn/courses/30/lessons/250125 [PCCE 기출문제] 9번 / 이웃한 칸

def solution(board, h, w):
    board_len= len(board)                   #보드 길이 저장
    count = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]   #h, w값의 변화량
    color = board[h][w]
    
    for i in range(0,4):
        if h+dh[i] >= board_len or w+dw[i] >= board_len or h+dh[i] == -1 or w+dw[i] == -1:
            continue                                        #파이썬에서 list[-1]은 마지막 원소를 의미하므로 처리
        else:
            if board[h+dh[i]][w+dw[i]] == color:
                count += 1
    
    return count