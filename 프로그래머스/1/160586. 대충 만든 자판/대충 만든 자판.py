def solution(keymap, targets):
    answer = []
    min_keymap = {}

    for key in keymap:
        for index, value in enumerate(key):
            if value not in min_keymap or min_keymap[value] > index + 1:
                min_keymap[value] = index + 1

    for input in targets:
        total = 0
        for i in input:
            key_buf = min_keymap.get(i, -1)
            if key_buf == -1:
                answer.append(-1)
                break
            else:
                total += key_buf
        else:
            answer.append(total)
    return answer