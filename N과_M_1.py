N,M = map(int,input().split())
num = []
perm = [None] * M
used = [0] * N
for i in range(1,N+1):
    num.append(i)

def permutation(idx):
    if idx == M:
        for i in perm:
            print(i,end = " ")
        print()
        return
    
    for i in range(N):
        if not used[i]:
            perm[idx] = num[i]
            used[i] = 1
            permutation(idx + 1)
            used[i] = 0

permutation(0)