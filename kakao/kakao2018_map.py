def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        char = ''
        binary = str(bin(arr1[i] | arr2[i]))[2:].zfill(n)
        for b in binary:
            if b == '1':
                char += '#'
            else:
                char += ' '
        answer.append(char)

    return answer

if __name__ == "__main__":
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])) # ["#####","# # #", "### #", "# ##", "#####"]
    print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])) # ["######", "###  #", "##  ##", " #### ", " #####", "### # "]