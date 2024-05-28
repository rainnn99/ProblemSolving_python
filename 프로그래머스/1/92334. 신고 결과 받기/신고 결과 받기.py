def solution(id_list, report, k):
    answer = []
    id = {key: 0 for key in id_list}
    total_report = {key: 0 for key in id_list}
    decl = {}

    for rep in report:
        value, key = rep.split()
        if key not in decl:
            decl[key] = set()
        decl[key].add(value)

    for key in decl:
        decl[key] = list(decl[key])

    for rep in decl.keys():
        if rep in total_report:
            total_report[rep] = len(decl[rep])

    for i in total_report.keys():
        if total_report[i] >= k:
            for key in decl[i]:
                id[key] += 1

    answer = list(id.values())

    return answer