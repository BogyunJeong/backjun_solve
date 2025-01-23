N = int(input())
X = list(map(int,input().split()))

dic = {a:b for b,a in enumerate((set(X)))}
print(dic)
for i in range(N):
    print(dic[X[i]],end = " ")
