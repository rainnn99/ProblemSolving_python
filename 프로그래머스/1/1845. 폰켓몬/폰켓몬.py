def solution(nums):
    buf = set(nums)
    if len(buf) >= len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = len(buf)
    return answer