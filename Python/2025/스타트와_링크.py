import sys

N = int(sys.stdin.readline())
r = int(N//2) # NCr 조합 구하기 위한 변수

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
num = [i for i in range(1,N+1)] # 사람 리스트 생성 [1,2,3,4,5,6...N] N명 까지  
min_value = 1e9 # 최소값 변수

def combinations(num,r,idx = 0, combi = []): # 조합 시작
    global min_value
    if len(combi) == r: 
        teamA = combi # 조합으로 뽑은 사람을 팀 A
        teamB = []
        for i in num:
            if not i in teamA:
                teamB.append(i) # 팀 B도 만들어줌
        S1 = 0
        S2 = 0
        for i in range(len(teamA)-1):
            for j in range(i+1,len(teamA)):
                a = teamA[i] -1 # 인덱스 맞춰주기 위해 1 뻄뻄
                b = teamA[j] -1
                c = teamB[i] -1
                d = teamB[j] -1
                S1 = arr[a][b] + arr[b][a] + S1 # Sij + Sji 로 합 구해줌
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