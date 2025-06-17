import sys
from collections import deque

N,M,v = map(int,sys.stdin.readline().split())

graph = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()

def dfs(graph,v,visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v,end =" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True # 현재 노드를 방문처리
    
    while queue: # 큐가 빌떄까지 반복
        v = queue.popleft()
        print(v,end = ' ')
        
        #해당 원소와 연결된 , 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (N+1)
dfs(graph,v,visited)
print()
visited = [False] * (N+1)
bfs(graph,v,visited)