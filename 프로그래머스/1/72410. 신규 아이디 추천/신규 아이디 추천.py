import re


def solution(new_id):
    # 1st
    new_id = new_id.lower()
    # 2nd
    pattern = r"[^a-z0-9.\-_]"
    new_id = re.sub(pattern, "", new_id)
    # 3rd
    pattern = r"\.{2,}"
    new_id = re.sub(pattern, '.', new_id)
    # 4th
    try:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:len(new_id)-1]
    except:
        pass
    # 5th
    if not new_id:
        new_id = 'a'
    # 6th
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7th
    if len(new_id) <= 2:
        for _ in range(3-len(new_id)):
            new_id += new_id[-1]

    return new_id