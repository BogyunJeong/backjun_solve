N = int(input())
vps = []
for i in range(N):
    X = input()
    isvps = True
    for j in X:
        if j == ')':
            if len(vps) == 0:
                isvps = False
            else:
                vps.pop()
        else:
            vps.append('(')
    if len(vps) == 0 and isvps :
        print('YES')
    else:
        print('NO')