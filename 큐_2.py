import sys
from collections import deque

d = deque()

N = int(sys.stdin.readline())

for i in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        d.append(command[1])
    elif command[0] == 'pop':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(d))
    elif command[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)
