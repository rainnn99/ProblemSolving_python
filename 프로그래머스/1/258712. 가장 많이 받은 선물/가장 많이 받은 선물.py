def solution(friends, gifts):
    gift_score = {value: 0 for value in friends}
    gift_record = {friend: {} for friend in friends}
    gift_pred = [0 for _ in friends]

    for i in gifts:
        sender, receiver = i.split(" ")[0], i.split(" ")[1]
        gift_score[sender] += 1
        gift_score[receiver] -= 1
        if receiver in gift_record[sender]:
            gift_record[sender][receiver] += 1
        else:
            gift_record[sender][receiver] = 1

    for i in range(len(friends)):
        buf1 = friends[i]
        for j in range(i+1, len(friends)):
            buf2 = friends[j]
            send = gift_record[buf1][buf2] if buf2 in gift_record[buf1] else 0
            receive = gift_record[buf2][buf1] if buf1 in gift_record[buf2] else 0
            if send > receive:
                gift_pred[i] += 1
            elif send < receive:
                gift_pred[j] += 1
            elif send == receive:
                send_score, receive_score = gift_score[buf1], gift_score[buf2]
                if send_score > receive_score:
                    gift_pred[i] += 1
                elif send_score < receive_score:
                    gift_pred[j] += 1

    return max(gift_pred)