from collections import deque
import sys


def bfs(graph):
    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i,j))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            elif graph[nx][ny] == -1:
                continue
            elif graph[nx][ny] > graph[x][y] + 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny)) 
            elif graph[nx][ny] != 0:
                continue
            
            queue.append((nx,ny))
            graph[nx][ny] = graph[x][y] + 1

def max_day(graph):
    max_value = 0
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1
            else:
                if graph[i][j] > max_value:
                    max_value = graph[i][j]
    else:
        return max_value



M,N = map(int,sys.stdin.readline().split())
graph =[list(map(int,sys.stdin.readline().split())) for _ in range(N)]


start = bfs(graph)

result = max_day(graph)
if result == -1:
    print(-1)
else:
    print(result-1)
