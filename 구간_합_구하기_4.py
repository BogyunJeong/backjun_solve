import sys

N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

# 전체 합 구하기
total_sum = 0
lst = []
for i in range(N):
    total_sum += arr[i]
    lst.append(total_sum)
#부분 합 구하기
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    result = lst[b] - lst[a-1]
    print(result)
