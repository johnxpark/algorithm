def count_traffic(time, logs):
    start = time
    end = time + 999
    count = 0
    for log in logs:
        if log[1] < start or end < log[0]:
            pass
        else:
            count += 1
    return count

def solution(lines):
    logs = []
    for line in lines:
        temp = line.split()
        end = temp[1].split(':')
        end[2] = end[2].split('.')
        end_ms = (int(end[0]) * 3600 + int(end[1]) * 60 + int(end[2][0])) * 1000 \
                + int(end[2][1])
        period_ms = int(float(temp[2][:-1]) * 1000)
        logs.append([end_ms - period_ms + 1, end_ms])

    answer = 0
    for log in logs:
        answer = max(answer, count_traffic(log[0], logs))
        answer = max(answer, count_traffic(log[1], logs))
    
    return answer


test_input = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
] # 7

test_input = [
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
] # 1

if __name__ == '__main__':
    print(solution(test_input))
    