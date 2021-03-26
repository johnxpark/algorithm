def solution(array, commands):
    answer = []

    for cmd in commands:
        new_array = array[cmd[0]-1: cmd[1]]
        new_array.sort()
        answer.append(new_array[cmd[2]-1])

    return answer

if __name__ == '__main__':
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	))  # [5, 6, 3]
