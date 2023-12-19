#https://school.programmers.co.kr/learn/courses/30/lessons/250137 [PCCP 기출문제] 1번 / 붕대 감기

def solution(bandage, health, attacks):
    max_health = health     #최대 체력
    time_buf = 0            #붕대 연속 성공시간
    
    attack = {attacks[0]:attacks[1] for attacks in attacks} #공격정보 저장 딕셔너리
    last_att = list(attack.keys())[-1]                      #마지막 공격 시간 저장
    
    for i in range(0, last_att+1):
        if i in attack:         # 공격 받을때
            health -= attack[i]
            time_buf = 0        #연속 성공시간 초기화
            if health <= 0:     #사망시 처리
                health = -1
                return health
        else:
            health += bandage[1]                                        #기본 초당 회복
            time_buf+=1                                                 #연속 성공시간 증가
            if time_buf//bandage[0] >= 1 and time_buf%bandage[0] == 0:  #추가 회복 조건 확인
                health += bandage[2]
            if health >= max_health:
                health = max_health                                     #최대 체력 제한
            
    return health