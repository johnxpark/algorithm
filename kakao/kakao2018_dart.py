import re

def solution(dartResult):
    result = re.findall('[0-9]+[SDT][*#]?', dartResult)
    score = [0, 0, 0]

    for i, dart in enumerate(result):
        score[i] = int(re.findall('[0-9]+', dart)[0])
        if dart.find('D') != -1:
            score[i] **= 2
        elif dart.find('T') != -1:
            score[i] **= 3
        if dart.find('*') != -1:
            score[i] *= 2
            if i != 0:
                score[i-1] *= 2
        elif dart.find('#') != -1:
            score[i] *= -1

    answer = sum(score)
    return answer

if __name__ == "__main__":
    print(solution("1S2D*3T"))      # 37
    print(solution("1D2S#10S"))     # 9
    print(solution("1D2S0T"))       # 3
    print(solution("1S*2T*3S"))     # 23
    print(solution("1D#2S*3S"))     # 5
    print(solution("1T2D3D#"))      # -4
    print(solution("1D2S3T*"))      # 59