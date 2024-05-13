def solution(park, routes):
    park_h, park_w = len(park), len(park[0])
    robot = []

    for i in range(park_h):
        for j in range(park_w):
            if park[i][j] == 'S':
                robot = [i, j]
    print(robot)
    for i in routes:
        direction, length = i.split(' ')
        length = int(length)
        count = 0
        if direction == 'E':
            if robot[1]+length < park_w:
                for mov in range(1, length+1):
                    if park[robot[0]][robot[1]+mov] == 'X':
                        count += 1
                if count == 0:
                    robot[1] += length
            else:
                continue
            
        elif direction == 'W':
            if robot[1]-length >= 0:
                for mov in range(1, length+1):
                    if park[robot[0]][robot[1]-mov] == 'X':
                        count += 1
                if count == 0:
                    robot[1] -= length
            else:
                continue
            
        elif direction == 'S':
            if robot[0]+length < park_h:
                for mov in range(1, length+1):
                    if park[robot[0]+mov][robot[1]] == 'X':
                        count += 1
                if count == 0:
                    robot[0] += length
            else:
                continue
            
        elif direction == 'N':
            if robot[0]-length >= 0:
                for mov in range(1, length+1):
                    if park[robot[0]-mov][robot[1]] == 'X':
                        count += 1
                if count == 0:
                    robot[0] -= length
            else:
                continue
    return robot