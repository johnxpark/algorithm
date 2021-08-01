def convert_to_minute(time):
    temp = list(map(int, time.split(':')))
    return temp[0] * 60 + temp[1]

def print_in_format(num):
    hour = num // 60
    minute = num % 60
    return f'{hour:02}:{minute:02}'

def solution(n, t, m, timetable):
    buses = []
    for i in range(0, n):
        buses.append(9 * 60 + t * i)

    crews = sorted(list(map(convert_to_minute, timetable)))

    last_bus = []
    idx_crew_boarded = []
    for i, bus in enumerate(buses):
        cnt = 0
        for j, crew in enumerate(crews):
            if cnt >= m:
                break
            if crew <= bus and j not in idx_crew_boarded:
                cnt += 1
                idx_crew_boarded.append(j)
                if i == len(buses) - 1:
                    last_bus.append(crew)
                # print(f'crew({crew}) boards bus({bus}) ({cnt}/{m})')

    if len(last_bus) == m:
        return print_in_format(last_bus[-1] - 1)
    else:
        return print_in_format(buses[-1])

if __name__ == "__main__":
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])) # "09:00"
    print(solution(2, 10, 2, ["09:10", "09:09", "08:00"])) # "09:09"
    print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])) # "08:59"
    print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])) # "00:00"
    print(solution(1, 1, 1, ["23:59"])) # "09:00"
    print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])) # "18:00"
    print(solution(10, 1, 5, ["09:00", "09:00", "09:00", "09:00", "09:00"])) # "09:09"
    print(solution(1, 1, 5, ["00:00", "00:00", "00:00", "00:00", "00:01", "00:02", "00:03", "00:04"])) # "00:00"
   