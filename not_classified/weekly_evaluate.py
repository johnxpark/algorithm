def solution(scores):
    answer = ''

    ### transpose using zip
    stu_scores = list(map(list, zip(*scores)))
    print(stu_scores)
    ###

    for i in range(len(scores)):
        my_score = []
        for j in range(len(scores)):
            my_score.append(scores[j][i])

        if (max(my_score) == my_score[i] and my_score.count(my_score[i]) == 1) or \
           (min(my_score) == my_score[i] and my_score.count(my_score[i]) == 1):
            my_score.pop(my_score.index(my_score[i]))

        avg_score = sum(my_score) / len(my_score)

        if avg_score >= 90:
            answer += 'A'
        elif avg_score >= 80:
            answer += 'B'
        elif avg_score >= 70:
            answer += 'C'
        elif avg_score >= 50:
            answer += 'D'
        else:
            answer += 'F'
    
    return answer

if __name__ == "__main__":
    # print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])) # "FBABD"
    # print(solution([[50,90],[50,87]])) # "DA"
    print(solution([[70,49,90],[68,50,38],[73,31,100]])) # "CFD"