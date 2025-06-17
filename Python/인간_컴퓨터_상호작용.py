import sys

S = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
p = {0 : [0] * 26}

for i,j in enumerate(S) :
    p[i+1] = p[len(p) - 1][:]
    p[i+1][ord(j)-97] += 1



for i in range(N):
    a,b,c = sys.stdin.readline().rstrip().split()
    a = ord(a) - 97

    result = p[int(c)+1][a] - p[int(b)][a]
    print(result)