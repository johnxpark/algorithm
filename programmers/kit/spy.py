def solution(clothes):
    table = {}
    for c in clothes:
        if c[1] not in table:
            table[c[1]] = 1
        else:
            table[c[1]] += 1

    answer = 1
    for t in table.values():
        answer *= (t + 1)

    return (answer - 1)

if __name__ == "__main__":
    print(solution([["yellowhat", "headgear"], \
                    ["bluesunglasses", "eyewear"], \
                    ["green_turban", "headgear"]])) # 5
    print(solution([["crowmask", "face"], \
                    ["bluesunglasses", "face"], \
                    ["smoky_makeup", "face"]])) # 3
                    