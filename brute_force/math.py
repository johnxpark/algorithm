def solution(answers):
    scores = [0] * 3
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, answer in enumerate(answers):
        if pattern1[i % 5] == answer:
            scores[0] += 1
        if pattern2[i % 8] == answer:
            scores[1] += 1
        if pattern3[i % 10] == answer:
            scores[2] += 1
    
    answer = []
    for i, score in enumerate(scores):
        if score == max(scores):
            answer.append(i + 1)

    return answer

if __name__ == "__main__":
    print(solution([1,2,3,4,5]))    # [1]
    print(solution([1,3,2,4,2]))    # [1, 2, 3]
