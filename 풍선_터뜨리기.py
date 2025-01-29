import sys
from collections import deque
N = int(sys.stdin.readline())
d = deque(enumerate(map(int,sys.stdin.readline().split())))
result = []
for i in range(N):
    a,b = d.popleft()
    result.append(a+1)
    if b > 0:
        d.rotate(-(b-1)) # 풍선을 pop 했기 떄문에 이미 왼쪽으로 1칸 회전된 상태이므로 -1 해줌

    else:
        d.rotate(-b)

for i in result:
    print(i,end = " ")

    




