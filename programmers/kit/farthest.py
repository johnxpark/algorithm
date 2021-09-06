import heapq

def dijkstra(graph, n, s):
    distance = [float('inf') for _ in range(n + 1)]
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + 1
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))
    return distance

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        graph[e[0]].append((e[1], 1))
        graph[e[1]].append((e[0], 1))

    distance = dijkstra(graph, n, 1)

    res = []
    max_dist = 0
    for i in range(1, n + 1):
        if distance[i] > max_dist:
            max_dist = distance[i]
            res = [i]
        elif distance[i] == max_dist:
            res.append(i)
        
    return len(res)

if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) # 3