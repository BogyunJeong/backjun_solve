N,M = map(int,input().split())
h = []
s = []
for i in range(N):
    h.append(input())

for i in range(M):
    s.append(input())
dic = {}
for i in s:
    dic[i] = int(0)

result = []

for i in h :
    if i in dic:
        result.append(i)

result.sort()
print(len(result))
for i in result:
    print(i)
