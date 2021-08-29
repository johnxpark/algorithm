import pprint

def is_answer(b: list, i: int, j: int, x_size: int, y_size: int) -> bool:
    size = len(b)
    value = -1
    zero = 0
    for x in range(i, i + x_size):
        for y in range(j, j + y_size):
            if b[x][y] == 0:
                if sum(b[x][:y]) != 0:
                    return False
                zero += 1
                if zero > 2:
                    return False
            else:
                if value == -1:
                    value = b[x][y]
                else:
                    if b[x][y] != value:
                        return False

    for x in range(size):
        for y in range(size):
            if b[x][y] == value:
                b[x][y] = 0

    return True

def solution(board):
    b = list(map(list, zip(*board)))
    size = len(b)
    answer = 0

    while True:
        target = -1
        for i in range(size):
            for j in range(size):
                if i < size - 2 and j < size - 1:
                    if is_answer(b, i, j, 3, 2):
                        target = b[i][j]
                        answer += 1
                        break
                if i < size - 1 and j < size - 2:
                    if is_answer(b, i, j, 2, 3):
                        target = b[i][j]
                        answer += 1
                        break
            if target != -1:
                break
        if target == -1:
            break     
    
    return answer

if __name__ == "__main__":
    print(solution([[0,0,0,0,0,0,0,0,0,0],\
                    [0,0,0,0,0,0,0,0,0,0],\
                    [0,0,0,0,0,0,0,0,0,0],\
                    [0,0,0,0,0,0,0,0,0,0],\
                    [0,0,0,0,0,0,4,0,0,0],\
                    [0,0,0,0,0,4,4,0,0,0],\
                    [0,0,0,0,3,0,4,0,0,0],\
                    [0,0,0,2,3,0,0,0,5,5],\
                    [1,2,2,2,3,3,0,0,0,5],\
                    [1,1,1,0,0,0,0,0,0,5]])) # 2
