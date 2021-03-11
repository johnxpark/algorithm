def solution(n, lost, reserve):
    answer = 0
    if lost == []:
        return n
    if reserve == []:
        return (n - len(lost))
    for l in reversed(lost):
        if l in reserve:
            lost.pop()
            reserve.remove(l)
        elif (l + 1) in reserve:
            if (l + 1) not in lost:
                lost.pop()
                reserve.remove(l + 1)
        elif (l - 1) in reserve:
            if (l - 1) not in lost:
                lost.pop()
                reserve.remove(l - 1)
    answer = n - len(lost)
    return answer

if __name__ == "__main__":
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    print(solution(n, lost, reserve))   # 5
