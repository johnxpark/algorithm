import heapq

def solution(jobs):
    length = len(jobs)
    answer = 0
    now = 0

    while len(jobs) > 0:
        h = []
        for job in jobs:
            if job[0] > now:
                continue
            if job[0] <= now:
                heapq.heappush(h, [job[1], job[0]])
        if len(h) > 0:
            next = heapq.heappop(h)
            if next[1] == now:
                answer += next[0]
            else:
                answer += now - next[1] + next[0]
            now += next[0]
            jobs.pop(jobs.index([next[1], next[0]]))
        else:
            now += 1

    return int(answer / length)

if __name__ == "__main__":
    print(solution([[0, 3], [1, 9], [2, 6]])) # 9