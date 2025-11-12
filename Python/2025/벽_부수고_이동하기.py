from collections import deque
import copy

def bfs():
    queue = deque()
    queue.append([0,0,0])
    visited[0][0][0] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y,w = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][w]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0<= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx,ny,w])
                elif graph[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w+1] = visited[x][y][w] + 1
                    queue.append((nx,ny,w+1))
    return -1

N,M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

print(bfs())

'''
[[[1, 3], [2, 4], [3, 5], [4, 6], [5, 7]], 
[[0, 12], [0, 11], [0, 10], [0, 9], [6, 6]],
[[11, 3], [10, 4], [9, 5], [8, 6], [7, 7]], 
[12, 4], [0, 13], [0, 10], [0, 9], [0, 8]], 
[[13, 5], [0, 16], [0, 17], [0, 0], [0, 0]], 
[[14, 6], [15, 7], [16, 8], [0, 17], [0, 18]]]

[[[1, 3], [0, 2], [0, 3], [0, 4]], 
[[0, 2], [0, 0], [0, 0], [0, 5]], 
[[0, 0], [0, 8], [0, 7], [0, 6]], 
[[0, 10], [0, 9], [0, 8], [0, 7]],
[[0, 11], [0, 0], [0, 0], [0, 0]], 
[[0, 12], [0, 13], [0, 14], [0, 15]]]

'''