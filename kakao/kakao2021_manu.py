from itertools import combinations

def solution(orders, course):
    d = {}
    for order in orders:
        li = [char for char in order]
        li.sort()
        for i in range(1, len(li) + 1):
            c = list(combinations(li, i))
            for j in range(len(c)):
                if len(c[j]) > 1:
                    if c[j] not in d:
                        d[c[j]] = 1
                    else:
                        d[c[j]] += 1

    res = {}
    for i, c in enumerate(course):
        for k, v in d.items():
            if v < 2:
                continue
            if len(k) == c:
                if c not in res:
                    res[c] = [(k, v)]
                else:
                    if v > res[c][0][1]:
                        res[c] = [(k, v)]
                    elif v == res[c][0][1]:
                        res[c].append((k, v))

    answer = []
    for val in res.values():
        for v in val:
            answer.append("".join(v[0]))
    answer.sort()

    return answer

if __name__ == "__main__":
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], \
                   [2,3,4])) # ["AC", "ACDE", "BCFG", "CDE"]
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], \
                   [2,3,5])) # ["ACD", "AD", "ADE", "CD", "XYZ"]
    print(solution(["XYZ", "XWY", "WXA"], \
                   [2,3,4])) # ["WX", "XY"]
