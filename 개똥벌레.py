import sys
N,H = map(int,sys.stdin.readline().split())

arr = [0 for i in range(H+1)]

for i in range(1,N+1):
    a = int(input())
    if i % 2 == 0:
        arr[H] -= 1
        arr[H-a] +=1
    else:
        arr[0] += 1
        arr[a] -= 1

for i in range(len(arr)-1):
    arr[i+1] += arr[i]

arr = arr[0:H]
cnt = 0


print(min(arr),arr.count(min(arr))) 