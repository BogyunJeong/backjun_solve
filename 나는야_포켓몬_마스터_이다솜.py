import sys
N,M = map(int,input().split())

d = {}
for i in range(1,N+1):
    d[i] = input()

dic = {v:k for k,v in d.items()}

for i in range(M):
    ans = input()
    if ans.isdigit():
        print(d[int(ans)])
    else:

        print(dic[ans])