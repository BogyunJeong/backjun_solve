import sys

N = int(sys.stdin.readline())
r = int(N//2)

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
num = [i for i in range(1,N+1)]
perm = [0] * int(N//2)  
used = [0] * N
min_value = 1e9

def combinations(num,r,idx = 0, combi = []):
    global min_value
    if len(combi) == r:
        teamA = combi
        teamB = []
        for i in num:
            if not i in teamA:
                teamB.append(i)
        S1 = 0
        S2 = 0
        for i in range(len(teamA)-1):
            for j in range(i+1,len(teamA)):
                a = teamA[i] -1 # 인덱스 맞춰주기 위해 1 뻄뻄
                b = teamA[j] -1
                c = teamB[i] -1
                d = teamB[j] -1
                S1 = arr[a][b] + arr[b][a] + S1
                S2 = arr[c][d] + arr[d][c] + S2
        if S1 > S2:
            S = S1 - S2
            if min_value > S:
                min_value = S
        elif S1 < S2:
            S = S2 - S1
            if min_value > S:
                min_value = S
        elif S1 == S2:
            min_value = 0        
        return
        
    for i in range(idx,N):
        combinations(num,r,i + 1,combi + [num[i]])
combinations(num,r)
print(min_value)