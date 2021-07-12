def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    answer = 0
    cache = []
    for city in [x.upper() for x in cities]:
        if city not in cache:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
            answer += 5
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
    return answer

if __name__ == "__main__":
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))    # 50
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))   # 21
    print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))   # 60
    print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))   # 52
    print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))    # 16
    print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))    # 25