def solution(price, money, count):
    answer = price * int(count * (count + 1) / 2) - money
    if answer < 0:
        return 0
    return answer

if __name__ == "__main__":
    print(solution(3, 20, 4)) # 10