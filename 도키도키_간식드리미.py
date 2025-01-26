import sys
N = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
stack = []
for i in L:
    stack.append(i)
    print(stack)