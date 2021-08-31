def is_valid(s: str):
    while s.find('[]') != -1 or s.find('{}') != -1 or s.find('()') != -1:
        s = s.replace('[]','').replace('{}','').replace('()','')
    if len(s) == 0:
        return 1
    else:
        return 0

def solution(s):
    answer = 0
    
    if len(s) % 2 != 0:
        return 0
    
    answer += is_valid(s)
    for _ in range(len(s) - 1):
        s = s[1:] + s[0]
        answer += is_valid(s)
        
    return answer

print(solution('[](){}'))
print(solution('}]()[{'))
print(solution('[)(]'))
print(solution('}}}'))
print(solution('[(])'))