dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def solution(rows, columns, queries):
    m = []
    for r in range(rows):
        m.append([c + 1 + r * columns for c in range(columns)])

    answer = []
    for query in queries:
        d = 0
        pr = query[0] - 1
        pc = query[1] - 1
        prev = m[pr][pc]
        minimum = prev
        while True:
            pr += dr[d]
            pc += dc[d]

            prev, m[pr][pc] = m[pr][pc], prev
            if prev < minimum:
                minimum = prev
            
            if pc + dc[d] == query[3] or pc + dc[d] == (query[1] - 2) or pr + dr[d] == query[2] or pr + dr[d] == (query[0] - 2):
                d += 1
            if d > 3:
                break
        answer.append(minimum)
    
    return answer

if __name__ == "__main__":
    print(solution(6, 6, [[2,2,5,4]])) # [8]
    print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # [8, 10, 25]
    print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])) # [1, 1, 5, 3]
    print(solution(100, 97, [[1,1,100,97]])) # [1]
