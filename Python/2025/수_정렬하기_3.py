N = int(input())
a = [0] * 10001

for _ in range(N):
    num = int(input())
    a[num] +=1

for i in range(1,N):
    if a[i]!=0:
        for _ in range(a[i]):
            print(i)