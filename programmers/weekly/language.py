def solution(table: list, languages: list, preference: list):
    jobs = []
    for t in table:
        tmp = t.split()
        jobs.append(tmp)

    answer = jobs[0][0]
    max_score = -1
    for job in jobs:
        score = 0
        for i, lang in enumerate(languages):
            if lang in job:
                score += preference[i] * (6 - job.index(lang))
        if score == max_score:
            if answer > job[0]:
                answer = job[0]
        elif score > max_score:
            max_score = score
            answer = job[0]
            
    return answer

if __name__ == "__main__":
    print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#",\
                    "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",\
                    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",\
                    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",\
                    "GAME C++ C# JAVASCRIPT C JAVA"],\
                    ["PYTHON", "C++", "SQL"],\
                    [7, 5, 5])) # "HARDWARE" 
    print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", \
                   "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", \
                   "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",\
                   "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",\
                   "GAME C++ C# JAVASCRIPT C JAVA"],\
                   ["JAVA", "JAVASCRIPT"],\
                   [7, 5])) # PORTAL
                 