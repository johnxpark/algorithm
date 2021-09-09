def compress(s, w):
    res = ''
    cnt = 1
    i = 0
    while i < len(s):
        if i + w > len(s):
            res += s[i:]
            break
        pat = s[i:i+w]

        if s[i+w:i+2*w] == pat:
            cnt += 1
        else:
            if cnt != 1:
                res += str(cnt) + pat
                cnt = 1
            else:
                res += pat
        i += w

    return res

def solution(s):
    end = len(s) // 2 + 1
    if len(s) < 3:
        end += 1

    res = []
    for i in range(1, end):
        res.append(len(compress(s, i)))

    return min(res)

if __name__ == "__main__":
    print(solution("aabbaccc")) # 7
    print(solution("ababcdcdababcdcd")) # 9
    print(solution("abcabcdede")) # 8
    print(solution("abcabcabcabcdededededede")) # 14
    print(solution("xababcdcdababcdcd")) # 17
