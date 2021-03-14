def solution(name):
    answer = 0
    table = [min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name]
    i = 0

    while True:
        answer += table[i]
        table[i] = 0

        if sum(table) == 0:
            break

        right = 1
        while True:
            if table[i + right] != 0:
                break
            right += 1
        left = 1
        while True:
            if table[i - left] != 0:
                break
            left += 1
        if left < right:
            i -= left
            answer += left
        else:
            i += right
            answer += right

    return answer

if __name__ == "__main__":
    name = "JEROEN"
    print(solution(name))   # 56
    name = "JAN"
    print(solution(name))   # 23
    name = "BBAB"
    print(solution(name))   # 6
