def solution(today, terms, privacies):
    answer = []
    term = {}
    for i in terms:
        key, value = i.split(" ", 1)
        term[key] = value

    year, month, day = today.split(".", 2)
    standard_day = int(year + month + day)

    for i, priv in enumerate(privacies):
        day_buf, term_buf = priv.split(" ")
        year_buf, month_buf, day_buf = [date for date in day_buf.split(".")]
        month_buf = int(month_buf) + int(term[term_buf])
        d_year, d_month = divmod(month_buf, 12)
        if not d_month:
            d_year -= 1
            d_month += 12
        year_buf = int(year_buf) + d_year
        if d_month < 10:
            month_buf = '0' + str(d_month)
        else:
            month_buf = str(d_month)
        priv_day = int(f'{year_buf}{month_buf}{day_buf}')
        if priv_day <= standard_day:
            answer.append(i+1)

    return answer