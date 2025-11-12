N = int(input())

for i in range(N):
    stack = []
    P = input()
    result = True
    for j in P:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                result = False
                break
    
    if len(stack) > 0:
        result = False

    if result:
        print('YES')
    else:
        print('NO')