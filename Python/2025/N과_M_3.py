N,M = map(int,input().split())
num = [i for i in range(1,N+1)]
perm = [None] * M

def permutation(idx):
    if idx == M:
        print(" ".join(map(str,perm)))
        return
    
    for i in range(N):
        perm[idx] = num[i]
        permutation(idx+1)

permutation(0)