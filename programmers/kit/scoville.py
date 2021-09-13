import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    answer = 0
    while True:      
        s0 = heapq.heappop(scoville)
        s1 = heapq.heappop(scoville)
        answer += 1
        heapq.heappush(scoville, s0 + 2 * s1)
        if scoville[0] >= K:
            return answer
        if len(scoville) == 1:
            return -1

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7)) # 2