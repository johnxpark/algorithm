def solution(food_times: list, k: int):
    if sum(food_times) <= k:
        return -1
    
    food_times = [[food_times[i], i + 1] for i in range(len(food_times))]
    food_times.sort()

    prev = 0
    for i, food in enumerate(food_times):
        if food[0] - prev > 0:
            chunk = (food[0] - prev) * (len(food_times) - i)
            if k >= chunk:
                prev = food[0]
                k -= chunk
            else:
                k %= len(food_times) - i
                new_food_times = food_times[i:]
                new_food_times.sort(key=lambda x: x[1])
                return new_food_times[k][1]

if __name__ == "__main__":
    print(solution([3, 1, 2], 5)) # 1