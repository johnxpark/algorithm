import re

def get_union(str):
    union = []
    for i in range(0, len(str) - 1):
        temp = str[i] + str[i + 1]
        if re.search('[a-zA-Z][a-zA-Z]', temp):
            union.append(temp.upper())
    return union
    
def solution(str1, str2):
    union1 = get_union(str1)
    union2 = get_union(str2)

    intersection = []
    sum_of_set = []
    for entry in union1:
        if entry in union2:
            intersection.append(entry)
            sum_of_set.append(entry)
            union2.remove(entry)
        else:
            sum_of_set.append(entry)
    sum_of_set += union2

    if len(intersection) == 0 and len(sum_of_set) == 0:
        answer = 65536
    else:
        answer = int((len(intersection) / len(sum_of_set)) * 65536)
    return answer

if __name__ == "__main__":
    print(solution("FRANCE", "french"))         # 16384
    print(solution("handshake", "shake hands")) # 65536
    print(solution("aa1+aa2", "AAAA12"))        # 43690
    print(solution("E=M*C^2", "e=m*c^2"))       # 65536