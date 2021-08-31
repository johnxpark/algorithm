def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))

    for i in range(len(numbers) -1):
        j = i + 1
        while j < len(numbers):
            if int(numbers[i] + numbers[j]) < int(numbers[j] + numbers[i]):
                numbers[i], numbers[j] = numbers[j] , numbers[i]
            else:
                pass
            j += 1

    answer = str(int(''.join(numbers)))
    return answer

if __name__ == '__main__':
    print(solution([6, 10, 2]))         # 6210
    print(solution([3, 30, 34, 5, 9]))  # 9534330
    print(solution([21, 212]))
    print(solution([0, 0, 0, 0]))
