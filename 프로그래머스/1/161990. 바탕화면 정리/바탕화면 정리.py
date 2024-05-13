def solution(wallpaper):
    bufx = []
    bufy = []
    for i in range(len(wallpaper)):
        lbuf = wallpaper[i].find('#')
        rbuf = wallpaper[i].rfind('#')
        if lbuf != -1:
            bufx.append(lbuf)
            bufx.append(rbuf)
            bufy.append(i)
    answer = [min(bufy), min(bufx), max(bufy)+1, max(bufx)+1]
    return answer