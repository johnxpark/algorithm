import sys
sys.setrecursionlimit(300000)

answer = 0

def dfs(a, adjacent_list, prev_node, node):
    global answer
    for next_node in adjacent_list[node]:
        if next_node != prev_node:
            dfs(a, adjacent_list, node, next_node)
    a[prev_node] += a[node]
    answer += abs(a[node])
    a[node] = 0

def solution(a, edges):
    global answer

    if sum(a) != 0:
        return -1

    adjacent_list = [[] for _ in range(len(a))]
    for m, n in edges:
        adjacent_list[m].append(n)
        adjacent_list[n].append(m)

    dfs(a, adjacent_list, 0, 0)
        
    return answer

if __name__ == '__main__':
    print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))   # 9
    answer = 0
    print(solution([1,2,3,-6], [[0,2],[1,2],[2,3]]))           # 9
    answer = 0
    print(solution([0,1,0], [[0,1],[1,2]]))                    # -1