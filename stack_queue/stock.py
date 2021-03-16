def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        while stack and (price < stack[-1][0]):
            element = stack.pop()
            answer[element[1]] = i - element[1]
        else:
            stack.append([price, i])
    while stack:
        element = stack.pop()
        answer[element[1]] = i - element[1]
    
    return answer

if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3])     # [4, 3, 1, 1, 0]
