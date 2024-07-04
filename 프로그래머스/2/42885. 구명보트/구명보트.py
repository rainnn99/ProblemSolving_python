def solution(people, limit):
    answer = 0
    people.sort()
    mini, maxi = 0, len(people) - 1

    while mini <= maxi:
        if people[mini] + people[maxi] <= limit:
            mini += 1

        maxi -= 1
        answer += 1

    return answer