import sys
from collections import deque
N = int(sys.stdin.readline())
d = deque(enumerate(map(int,sys.stdin.readline().split())))
result = []
for i in range(N):
    a,b = d.popleft()
    result.append(a+1)
    if b > 0:
        d.rotate(-(b-1))

    else:
        d.rotate(-b)

for i in result:
    print(i,end = " ")

    




