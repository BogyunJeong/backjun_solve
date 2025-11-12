
stack = []
N = int(input())

for i in range(N):
    a = list(input().split()) # 리스트로 받음 ['push', '1'] , ['top']
    if len(a) > 1:
        stack.append(int(a[1]))
    else:
        s = a[0]
        if s == 'pop':
            if len(stack):
                print(stack.pop())
            else:
                print(-1)

        elif s == 'size':
            print(len(stack))
        
        elif s == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif s == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
