from collections import deque
from itertools import combinations
from copy import deepcopy

def bfs(arr,virus_queue):
    queue = deque()
    queue.extend(virus_queue)
    
    while queue:
        r,w = queue.popleft()

        for k in range(4):
            nr = r + dr[k]
            nw = w + dw[k]

            if -1 < nr < n and -1 < nw < m:
                if arr[nr][nw] == 0:
                    queue.append((nr,nw))
                    arr[nr][nw] = 2


    

def check_safezone(arr):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1

    return cnt


n,m = map(int,input().split()) # n은 세로, m은 가로
graph = [list(map(int,input().split())) for _ in range(n)]

dr = [-1,1,0,0]
dw = [0,0,-1,1]

virus_queue = [] # 바이러스 담을 큐
empty_lst = [] # 벽 세울 수 있는 큐

for i in range(n): # 바이러스 좌표를 담기
    for j in range(m):

        if graph[i][j] == 2:
            virus_queue.append((i,j))
        elif graph[i][j] == 0:
            empty_lst.append((i,j))

wall = list(combinations(empty_lst,3))

result = 0 # 안전지대 최대값 계산
for a,b,c in wall:
    arr = deepcopy(graph)

    arr[a[0]][a[1]] = 1
    arr[b[0]][b[1]] = 1
    arr[c[0]][c[1]] = 1

    bfs(arr,virus_queue)

    cnt = check_safezone(arr)
    result = max(result,cnt)

print(result)
    
