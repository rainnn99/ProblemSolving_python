def solution(s):
    answer = 0
    match = {')': '(', '}': '{', ']': '['}

    for i in range(len(s)):
        buf1 = s[:i]
        buf2 = s[i:]
        stack = []

        for char in buf2 + buf1:
            if char in ('(', '{', '['):
                stack.append(char)
            else:
                if not stack:
                    break
                buf = stack.pop()
                if match[char] != buf:
                    break
        else:
            if not stack:
                answer += 1

    return answer