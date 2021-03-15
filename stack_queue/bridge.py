from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    weight_sum = 0
    bridge_queue = deque([0 for _ in range(bridge_length)])
    truck_queue = deque([i for i in truck_weights])

    while True:
        if len(bridge_queue) == 0 and len(truck_queue) == 0:
            break
        
        if len(bridge_queue) != 0:
            weight_sum -= bridge_queue.popleft()

        if len(truck_queue) == 0:
            pass
        elif (weight_sum + truck_queue[0]) <= weight:
            next_truck_weight = truck_queue.popleft()
            bridge_queue.append(next_truck_weight)
            weight_sum += next_truck_weight
        else:
            bridge_queue.append(0)

        answer += 1
    return answer

print(solution(2, 10, [7,4,5,6]))   # 8
print(solution(100, 100, [10]))     # 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))     # 110
