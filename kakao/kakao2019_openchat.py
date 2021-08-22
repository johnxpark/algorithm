def solution(record):
    names = {}
    temp = []

    for r in record:
        if r[0] == 'E':
            _, uid, name = r.split()
            names[uid] = name
            temp.append(['E', uid])
        elif r[0] == 'L':
            temp.append(['L', r.split()[1]])
        else:
            _, uid, name = r.split()
            names[uid] = name

    answer = []
    for t in temp:
        if t[0] == 'E':
            answer.append(f"{names[t[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{names[t[1]]}님이 나갔습니다.")

    return answer

if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", \
                    "Enter uid4567 Prodo", \
                    "Leave uid1234", \
                    "Enter uid1234 Prodo", \
                    "Change uid4567 Ryan"]))
    # ["Prodo님이 들어왔습니다.",
    #  "Ryan님이 들어왔습니다.",
    #  "Prodo님이 나갔습니다.",
    #  "Prodo님이 들어왔습니다."]