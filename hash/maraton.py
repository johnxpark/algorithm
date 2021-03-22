def solution(participant, completion):
    d = {}
    for p in participant:
        if p not in d:
            d[p] = 1
        else:
            d[p] += 1

    for c in completion:
        if d[c] == 1:
            d.pop(c)
        elif d[c] != 0:
            d[c] -= 1

    return list(d.keys())[0]

if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # "leo"
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], \
                   ["josipa", "filipa", "marina", "nikola"]))   # "vinko"
    print(solution(["mislav", "stanko", "mislav", "ana"], \
                   ["stanko", "ana", "mislav"]))                # "mislav"
