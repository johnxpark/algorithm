n = int(input())

lines = []
for _ in range(n):
    lines.append(list((map(list, input().split()))))

for line in lines:
    for i, word in enumerate(line):
        for char in reversed(word):
            print(char, end='')
        print(' ', end='')
        if i == (len(line) - 1):
            print('')
