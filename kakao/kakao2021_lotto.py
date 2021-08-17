SCORE = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

def solution(lottos, win_nums):
    hit, joker = 0, 0
    for l in lottos:
        if l in win_nums:
            hit += 1
        elif l == 0:
            joker += 1

    return [SCORE[hit + joker], SCORE[hit]]

if __name__ == "__main__":
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) # [3, 5]
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])) # [1, 6]
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])) # [1, 1]