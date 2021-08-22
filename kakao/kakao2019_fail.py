def solution(N: int, stages: list):
    stages_clear = [len(stages)]
    temp = []
    for i in range(1, N + 1):
        here = stages.count(i)
        clear = stages_clear[i - 1] - here
        stages_clear.append(clear)
        if here == 0 and clear == 0:
            temp.append([i, 0])
        else:
            temp.append([i, here / (here + clear)])

    temp.sort(key= lambda x : (-x[1], x[0]))

    answer = []
    for t in temp:
        answer.append(t[0])

    return answer

if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
    print(solution(4, [4, 4, 4, 4, 4])) # [4,1,2,3]
    print(solution(5, [2, 1, 2, 4, 2, 4, 3, 3])) # [4, 3, 2, 1, 5]