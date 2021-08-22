import pprint

def solution(relation):
    num_row = len(relation)
    num_col = len(relation[0])
    num_comb = 1 << num_col

    data = [[] for _ in range(num_comb)]
    flag = [True for _ in range(num_comb)]
    flag[0] = False

    for r in range(num_row):
        for k in range(1, num_comb):
            if flag[k] == False:
                continue
    
            s = []
            idx_bin = str(bin(k))[2:]
            idx_bin_list = list(idx_bin)
            idx_bin_list.reverse()
            
            for i in range(len(idx_bin_list)):
                if idx_bin_list[i] == '1':
                    s.append(relation[r][i])
            
            if s not in data[k]:
                data[k].append(s)
            else:
                flag[k] = False

    print(flag)
    pprint.pprint(data)

    candidate_key = []
    for i in range(len(flag)):
        if flag[i] == True:
            if len(candidate_key) == 0:
                candidate_key.append(i)
            else:
                is_unique = True
                for key in candidate_key:
                    if key & i == key:
                        is_unique = False
                        break
                if is_unique:
                    candidate_key.append(i)
    
    # print(candidate_key)
    return len(candidate_key)
     
if __name__ == "__main__":
    print(solution([["100","ryan","music","2"], \
                    ["200","apeach","math","2"], \
                    ["300","tube","computer","3"], \
                    ["400","con","computer","4"], \
                    ["500","muzi","music","3"], \
                    ["600","apeach","music","2"]])) # 2
    # print(solution([["a", "100","ryan","music","2"], \
    #                 ["b", "200","apeach","math","2"], \
    #                 ["c", "300","tube","computer","3"], \
    #                 ["d", "400","con","computer","4"], \
    #                 ["e", "500","muzi","music","3"], \
    #                 ["f", "600","apeach","music","2"]])) # 3
    # print(solution([["a","ryan","music","2"], \
    #                 ["b","apeach","math","2"], \
    #                 ["a","tube","computer","3"], \
    #                 ["a","con","computer","4"], \
    #                 ["b","muzi","music","3"], \
    #                 ["c","apeach","music","2"]])) # 3         a2 b2 a3 a4 b3 c2