MAP = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def translate(num):
    if num in MAP:
        return MAP[num]
    return str(num) 

def calculate(n, num):
    if num < n:
        return translate(num)

    result = ''
    while num >= n:
        remainder = translate(num % n)
        num //= n
        result = remainder + result
    return translate(num) + result

def solution(n, t, m, p):
    members = ['' for i in range(m + 1)]
    num = 0
    idx = 1
    while True:
        temp = calculate(n, num)
        while True:
            members[idx] += temp[0]
            if len(members[p]) >= t:
                return members[p]
            if len(temp) == 1:
                break
            temp = temp[1:]
            idx += 1
            if idx > m:
                idx = 1
        num += 1

if __name__ == "__main__":
    print(solution(2, 4, 2, 1)) # "0111"
    print(solution(16, 16, 2, 1)) # "02468ACE11111111"
    print(solution(16, 16, 2, 2)) # "13579BDF01234567"
