def solution(array, commands):
    answer = []
    for command in commands:
        buf = sorted(array[command[0]-1:command[1]])
        answer.append(buf[command[2]-1])
    return answer