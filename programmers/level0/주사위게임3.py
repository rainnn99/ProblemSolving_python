# https://school.programmers.co.kr/learn/courses/30/lessons/181916 주사위게임3
def solution(a,b,c,d):
    buf=[a,b,c,d]
    count = [0,0,0,0,0,0,0]
    answer = 0
    for i in range(len(buf)):
        count[buf[i]]+=1
        
    if count.count(4):
        i = count.index(4)
        answer = 1111*i
    elif count.count(3):
        i = count.index(3)
        j = count.index(1)
        answer = (10*i+j)**2
    elif count.count(2):
        buf2=[]
        buf3=[]
        for i in range(7):
            if count[i]==2:
                buf2.append(i)
            elif count[i]==1:
                buf3.append(i)
            print(f'i = {i}, count : {count}, buf2 = {buf2}, buf3={buf3}')
                
        if len(buf2)==2:
            answer = (buf2[0]+buf2[1]) * abs(buf2[0]-buf2[1])
        else:
            answer = buf3[0]*buf3[1]
    else:
        answer = count.index(1)
    return answer