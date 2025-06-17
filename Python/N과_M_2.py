N,M = map(int,input().split())

num = [i for i in range(1,N+1)]
perm = [None] * M

def permutation(idx,s):
    if idx == M:
        print(" ".join(map(str,perm)))
        return

    for i in range(s,N):
            perm[idx] = num[i]
            permutation(idx+1,i+1)
            
permutation(0,0)
