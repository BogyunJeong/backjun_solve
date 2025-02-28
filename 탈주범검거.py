from collections import deque

# 방향 정보 사전
pipe_directions = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],  # 상, 하, 좌, 우
    2: [(-1, 0), (1, 0)],  # 상, 하
    3: [(0, -1), (0, 1)],  # 좌, 우
    4: [(-1, 0), (0, 1)],  # 상, 우
    5: [(1, 0), (0, 1)],   # 하, 우
    6: [(1, 0), (0, -1)],  # 하, 좌
    7: [(-1, 0), (0, -1)]  # 상, 좌
}

reverse_directions = {
    (-1, 0): (1, 0),
    (1, 0): (-1, 0),
    (0, -1): (0, 1),
    (0, 1): (0, -1)
}

def solve(N, M, visited, L):
    global cnt
    cnt = sum(1 for i in range(N) for j in range(M) if 0 < visited[i][j] <= L)

def find_route(x, y):
    for dx, dy in pipe_directions[arr[x][y]]:
        nx, ny = x + dx, y + dy

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if visited[nx][ny] != 0 or arr[nx][ny] == 0:
            continue

        if reverse_directions[(dx, dy)] in pipe_directions[arr[nx][ny]]:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

def bfs(x, y):
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        find_route(x, y)

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    queue = deque()

    bfs(R, C)
    solve(N, M, visited, L)
    print(visited)
    print(f'#{tc} {cnt}')
