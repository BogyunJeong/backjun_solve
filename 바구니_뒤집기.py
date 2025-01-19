N,M = map(int,input().split())
baskets = [i+1 for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    for j in range((b-a+1)//2):
        baskets[a+1],baskets[b-1] = baskets[b-1], baskets[a+1]
    

for i in baskets:
    print(i,end = " ")        