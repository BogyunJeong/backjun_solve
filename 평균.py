N = int(input())

score = list(map(int,input().split()))
m = max(score)
new_s = []
for i in range(N):
    new_s.append(score[i] /m * 100)

print(round(sum(new_s)/N,5))