from collections import Counter


def solution(N, stages):
    failure_rate = {key: 0.0 for key in range(1, N + 1)}
    stage_progresss_buf = Counter(stages)
    stage_progresss = {key: stage_progresss_buf.get(key, 0) for key in range(1, N+1)}
    buf = len(stages)
    for key, value in stage_progresss.items():
        if buf != 0:
            failure_rate[key] = value / buf
            buf -= value
        else:
            break

    failure_rate = dict(sorted(failure_rate.items(), key=lambda item: item[1], reverse=True))
    print(failure_rate)
    answer = list(failure_rate.keys())

    return answer