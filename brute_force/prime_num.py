import itertools
import math

def solution(numbers):
    answer = 0
    chars = [s for s in numbers]

    nums = []
    for i in range(1, len(chars) + 1):
        nums.extend(list(map(int, map(''.join, itertools.permutations(chars, i)))))
    nums = list(set(nums))

    for num in nums:
        is_prime = True
        if num <= 1:
            continue
        if num == 2:
            answer += 1
            continue
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

    return answer

if __name__ == "__main__":
    print(solution('17'))    # 3 : 7, 17, 71
    print(solution('011'))   # 2 : 11, 101
