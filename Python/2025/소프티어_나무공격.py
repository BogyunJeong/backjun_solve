import sys

N,M = map(int,sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(2):
    a,b = map(int,sys.stdin.readline().split())
    for j in range(a-1,b):
        for k in range(M):
            if arr[j][k] == 1:
                arr[j][k] = 0
                break

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            result += 1

print(result)