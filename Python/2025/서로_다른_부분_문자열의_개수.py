import sys

S = sys.stdin.readline().rstrip()
arr = set()
N = len(S)

for i in range(N):
    for j in range(i+1,N+1):
        arr.add(S[i:j])

print(len(arr))

