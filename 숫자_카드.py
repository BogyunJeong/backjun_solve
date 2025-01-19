N = int(input())
card = list((map(int,input().split())))
card = set(card)
M = int(input())
num = list(map(int,input().split()))
result = [0] * M
for i in range(M):
    if num[i] in card:
        result[i] = 1

for i in result:
    print(i,end = " ")