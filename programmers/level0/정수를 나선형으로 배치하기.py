# https://school.programmers.co.kr/learn/courses/30/lessons/181832
def solution(n):
    answer = [[0 for _ in range(n)] for __ in range(n)]
    buf = 0
    x, y = 0, 0
    for i in range(1, n*n+1):
        answer[x][y] = i
        if(buf%4==0):
            if y+1==n or answer[x][y+1] != 0:
                buf+=1
                x+=1
            else:
                y+=1
        elif(buf%4==1):
            if x+1==n or answer[x+1][y] != 0:
                buf+=1
                y-=1
            else:
                x+=1
        elif(buf%4==2):
            if answer[x][y-1] != 0:
                buf+=1
                x-=1
            else:
                y-=1
        elif(buf%4==3):
            if answer[x-1][y] != 0:
                buf+=1
                y+=1
            else:
                x-=1
    return answer