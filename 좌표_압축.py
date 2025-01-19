N = int(input())
X = list(map(int,input().split()))
dic = {a:b for b,a in enumerate(sorted((set(X))))}

for i in range(N):
    print(dic[X[i]],end = " ")