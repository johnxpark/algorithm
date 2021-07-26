import re

class Info:
    def __init__(self, name, head, num):
        self.name = name
        self.head = head
        self.num = num

def to_change(file1, file2):
    if file1.head > file2.head:
        return True
    elif file1.head == file2.head:
        if file1.num > file2.num:
            return True
    return False

def solution(files):
    files = list(Info(f, re.findall('^[a-zA-Z-. ]+', f)[0].lower(), int(re.findall('[0-9]+', f)[0])) for f in files)

    for i in range(1, len(files)):
        for j in range(i, 0, -1):
            if to_change(files[j - 1], files[j]):
                files[j - 1], files[j] = files[j], files[j - 1]

    answer = list(f.name for f in files)
    return answer

if __name__ == "__main__":
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
    # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
