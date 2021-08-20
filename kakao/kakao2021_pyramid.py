import math

def solution(enroll, referral, seller, amount):
    nodes = {}
    for i in range(len(enroll)):
        nodes[enroll[i]] = {"referral": referral[i], "money": 0}

    ptr = ""
    for i in range(len(seller)):
        ptr = seller[i]
        money = amount[i] * 100
        while True:
            nodes[ptr]["money"] += int(math.ceil(money * 0.9))
            money = int(math.floor(money * 0.1))
            if money == 0:
                break
            ptr = nodes[ptr]["referral"]
            if ptr == "-":
                break

    answer = []
    for e in enroll:
        answer.append(nodes[e]["money"])

    return answer

if __name__ == "__main__":
    print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], \
                   ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], \
                   ["young", "john", "tod", "emily", "mary"], \
                   [12, 4, 2, 5, 10]))	# [360, 958, 108, 0, 450, 18, 180, 1080]
    print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], \
                   ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], \
                   ["sam", "emily", "jaimie", "edward"], \
                   [2, 3, 5, 4])) # [0, 110, 378, 180, 270, 450, 0, 0]