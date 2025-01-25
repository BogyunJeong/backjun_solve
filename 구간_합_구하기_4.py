import sys


N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
#전체 합 구하기
cnt = 0
allsum = [0]
for i in range(N):
    cnt += arr[i]
    allsum.append(cnt)

#부분 합 구하기
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    result = allsum[b] - allsum[a-1]
    print(result)
