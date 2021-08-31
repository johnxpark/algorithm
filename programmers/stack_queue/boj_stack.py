cmd = []
stack = []

n = int(input())
for i in range(n):
    cmd.append(list(input().split()))

for c in cmd:
    if c[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif c[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    else:
        stack.append(c[1])
