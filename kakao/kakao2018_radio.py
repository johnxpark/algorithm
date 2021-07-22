table = {"C#": "V", "D#": "W", "F#": "X", "G#": "Y", "A#": "Z"}

def convert_to_minute(time):
    temp = list(map(int, time.split(':')))
    return temp[0] * 60 + temp[1]

def replace_sharp(melody):
    for x in table:
        melody = melody.replace(x, table[x])
    return melody

def solution(m, musicinfos):
    m = replace_sharp(m)

    data = []
    for musicinfo in musicinfos:
        temp = list(musicinfo.split(','))
        temp[3] = replace_sharp(temp[3])
        melody = ''
        for i in range(convert_to_minute(temp[1]) - convert_to_minute(temp[0])):
            while i >= len(temp[3]):
                i -= len(temp[3])
            melody += temp[3][i]
        data.append([temp[2], melody])

    answer = ''
    length = 0
    for d in data:
        if m in d[1]:
            if len(d[1]) > length:
                answer = d[0]
                length = len(d[1])

    if answer:
        return answer
    else:
        return "(None)"


if __name__ == "__main__":
    print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))   # "HELLO"
    print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))   # "FOO"
    print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))   # "WORLD"