import sys
from collections import deque
N = int(sys.stdin.readline())
D = deque()

for i in range(1,N+1):
    D.append(i)

while len(D) != 1:
    D.popleft()
    D.rotate(-1)
for i in D:
    print(i)