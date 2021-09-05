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
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))
    return distance

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))
    nodes = [x for x in range(1, n + 1) if x != s]
    res = []

    distance_start = dijkstra(graph, n, s)
    res.append(distance_start[a] + distance_start[b])

    for via in nodes:
        distance = dijkstra(graph, n, via)
        res.append(distance_start[via] + distance[a] + distance[b])

    return min(res)
    
if __name__ == "__main__":
    print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])) # 82
    print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])) # 14
    print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])) # 18
