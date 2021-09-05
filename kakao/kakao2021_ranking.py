from bisect import bisect_left

def solution(info, query):
    d0 = {"-": 0, "cpp": 1, "java": 2, "python": 3}
    d1 = {"-": 0, "backend": 1, "frontend": 2}
    d2 = {"-": 0, "junior": 1, "senior": 2}
    d3 = {"-": 0, "chicken": 1, "pizza": 2}
    table = [[] for _ in range(108)]

    for i in info:
        i = i.split()
        i[4] = int(i[4])
        for v0 in [0, d0[i[0]]]:
            for v1 in [0, d1[i[1]]]:
                for v2 in [0, d2[i[2]]]:
                    for v3 in [0, d3[i[3]]]:
                        idx = v0 * 27 + v1 * 9 + v2 * 3 + v3
                        table[idx].append(i[4])

    for i in range(108):
        table[i].sort()

    answer = []
    for q in query:
        q = q.split()
        q[7] = int(q[7])
        idx = d0[q[0]] * 27 + d1[q[2]] * 9 + d2[q[4]] * 3 + d3[q[6]]
        answer.append(len(table[idx]) - bisect_left(table[idx], int(q[7])))

    return answer

if __name__ == "__main__":
    print(solution(["java backend junior pizza 150", \
                    "python frontend senior chicken 210", \
                    "python frontend senior chicken 150", \
                    "cpp backend senior pizza 260", \
                    "java backend junior chicken 80", \
                    "python backend senior chicken 50"],
                   ["java and backend and junior and pizza 100", \
                    "python and frontend and senior and chicken 200", \
                    "cpp and - and senior and pizza 250", \
                    "- and backend and senior and - 150", \
                    "- and - and - and chicken 100", \
                    "- and - and - and - 150"])) # [1,1,1,1,2,4]
