dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]

class TwoByTwoPattern:
    def __init__(self, r, c, value):
        self.r = r
        self.c = c
        self.value = value

def find_pattern(m, n, data):
    result = []
    for r in range(m - 1):
        for c in range(n - 1):
            if data[r][c] == 0:
                continue
            if data[r][c] == data[r][c + 1] and data[r][c] == data[r + 1][c] and data[r + 1][c] == data[r + 1][c + 1]:
                result.append(TwoByTwoPattern(r, c, data[r][c]))
    return result

def remove_pattern(patterns, data):
    result = 0
    for pattern in patterns:
        for i in range(4):
            if data[pattern.r + dx[i]][pattern.c + dy[i]] == pattern.value:
                data[pattern.r + dx[i]][pattern.c + dy[i]] = 0
                result += 1
    return result

def relocate(m, n, data):
    is_changed = True
    while is_changed:
        is_changed = False
        for r in range(1, m):
            for c in range(n):
                if data[r][c] == 0:
                    i = r - 1
                    while i >= 0:
                        if data[i][c] == 0:
                            i -= 1
                        else:
                            data[r][c] = data[i][c]
                            data[i][c] = 0
                            is_changed = True
                            break

def solution(m, n, board):
    data = list(map(list, board))
    answer = 0

    while True:
        patterns = find_pattern(m, n, data)
        if not patterns:
            break
        answer += remove_pattern(patterns, data)
        relocate(m, n, data)
    
    return answer

if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) # 14
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) # 15