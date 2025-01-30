import sys
from collections import deque

N = int(sys.stdin.readline())
D = deque()

for i in range(N):
    C = sys.stdin.readline().split()
    if C[0] == '1':
        D.appendleft(C[1])
    elif C[0] == '2':
        D.append(C[1])
    elif C[0] == '3':
        if D:
            print(D.popleft())
        else:
            print(-1)
    elif C[0] == '4':
        if D:
            print(D.pop())
        else:
            print(-1)
    elif C[0] == '5':
        print(len(D))
    elif C[0] == '6':
        if D:
            print(0)
        else:
            print(1)
    elif C[0] == '7':
        if D:
            print(D[0])
        else:
            print(-1)
    elif C[0] == '8':
        if D:
            print(D[-1])
        else:
            print(-1)