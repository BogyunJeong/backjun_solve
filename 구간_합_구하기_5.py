import sys

def prefix_sum(N):
    prefixSum = [[0]* (N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] + arr[i-1][j-1] - prefixSum[i-1][j-1]
    return prefixSum

N,M = map(int,sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
prefixSum = prefix_sum(N)

for i in range(M):
    a,b,c,d = map(int,sys.stdin.readline().split())
    partSum = prefixSum[c][d] - prefixSum[a-1][d] - prefixSum[c][b-1] + prefixSum[a-1][b-1]
    print(partSum)


