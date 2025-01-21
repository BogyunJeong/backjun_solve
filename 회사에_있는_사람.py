N = int(input())
arr = set()
for i in range(N):
    a,b = input().split()
    if b == 'enter':
        arr.add(a)
    elif b == 'leave':
        arr.remove(a)
arr = list(arr)
arr.sort(reverse = True)
for i in arr:
    print(i)
