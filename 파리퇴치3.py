N,M = map(int,input().split())
arr = []
result = 0
total = 0
for i in range(N):
    arr.append(list(map(int,input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

di = [1,-1,-1,1]
dj = [1,1,-1,-1]

for i in range(N):
    for j in range(N):
        cnt1 = arr[i][j]
        cnt2 = arr[i][j]

        for k in range(4):
            for l in range(1,M):
                a = i + dx[k] * l
                b = j + dy[k] * l

                c = i + di[k] * l
                d = j + dj[k] * l

                if -1 < a < N and -1 < b < N:
                    cnt1 += arr[a][b]
                if -1 < c < N and -1 < d < N:
                    cnt2 += arr[c][d]

        total = max(cnt1,cnt2)
        
        if  result < total:
            result = total 

print(result)
        
