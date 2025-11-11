from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(type,r1,c1,r2,c2,degree,board):
    queue = deque()
    queue.append((r1,c1))
    visited = [[0 for _ in range(1001)] for _ in range(1001)]

    while queue:
        r,c = queue.popleft()

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if visited[nx][ny]:
                continue
            if r1 <= nx <= r2 and c1 <= ny <= c2:
                if type == 1:
                    board[nx][ny] -= degree
                else:
                    board[nx][ny] += degree
                visited[nx][ny] = 1
                queue.append((nx,ny))




def solution(board, skill):
    for i in range(len(skill)):
       bfs(skill[i][0],skill[i][1],skill[i][2],skill[i][3],skill[i][4],skill[i][5],board)

    answer = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                answer += 1

    return answer


solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])