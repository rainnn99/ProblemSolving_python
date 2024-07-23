def solution(n, words):
    answer = [0, 0]
    buf = dict()
    last = words[0][0]

    for idx, word in enumerate(words):
        if last != word[0]:
            answer = [idx % n + 1, idx // n + 1]
            break
        last = word[-1]
        if word not in buf:
            buf[word] = 1
        else:
            answer = [idx % n + 1, idx // n + 1]
            break

    return answer