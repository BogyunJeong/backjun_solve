N = int(input())
card = list((map(int,input().split())))
M = int(input())
num = list(map(int,input().split()))


d = {}

for i in num:
    d[i] = int(0)
    
print(d)

for i in card:
    if i in d:
        d[i] +=1

for i in num:
    print(d[i],end = " ")