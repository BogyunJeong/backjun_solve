N,M = map(int,input().split())
arr = set()
a = []

for i in range(N):
    arr.add(input())
for i in range(M):
    a.append(input())

count = 0

for i in range(M):
    if a[i] in arr:
        count +=1

print(count)