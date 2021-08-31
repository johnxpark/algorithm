def solution(n, times):
    times.sort()
    start = 0
    end = times[-1] * n
    min_value = float('inf')

    while start <= end:
        mid = (start + end) // 2

        people = 0
        for t in times:
            people += mid // t
        # print(start, mid, end, people)
               
        if people >= n:
            end = mid - 1
            if mid < min_value:
                min_value = mid
        else:
            start = mid + 1

    return min_value

if __name__ == "__main__":
    print(solution(6, [7, 10])) # 28
