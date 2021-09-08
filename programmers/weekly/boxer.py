def solution(weights, head2head):
    res = {}
    for i, h2h in enumerate(head2head):
        win = h2h.count('W')
        no_match = h2h.count('N')
        if no_match == len(h2h):
            ratio = 0
        else:
            ratio = win / (len(h2h) - no_match)
        if ratio not in res:
            res[ratio] = [i+1]
        else:
            res[ratio].append(i+1)
    res = sorted(res.items(), key=lambda x: -x[0])

    answer = []  
    for ratio, boxers in res:
        if len(boxers) == 1:
            answer.append(boxers[0])
        else:
            tmp = []
            for b in boxers:
                upset = 0
                for i, h2h in enumerate(head2head[b-1]):
                    if h2h == 'W' and weights[b-1] < weights[i]:
                        upset += 1
                tmp.append([upset, weights[b-1], b])
            tmp = sorted(sorted(sorted(tmp, key=lambda x: x[2]), key=lambda x: -x[1]), key=lambda x: -x[0])
            for t in tmp:
                answer.append(t[2])

    return answer

if __name__ == "__main__":
    print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"])) # [3,4,1,2]
    print(solution([145,92,86], ["NLW","WNL","LWN"])) # [2,3,1] 
    print(solution([60,70,60], ["NNN","NNN","NNN"])) # [2,1,3]