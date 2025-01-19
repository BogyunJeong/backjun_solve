N = int(input())
arr = []
for i in range(N):
    word = input()
    arr.append((word,len(word)))
arr = list(set(arr))
arr = sorted(arr,key = lambda x:(x[1],x[0]))
for i in arr:
    print(i[0])
