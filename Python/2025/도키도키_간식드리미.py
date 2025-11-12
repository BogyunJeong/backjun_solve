import sys
N = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
treshold = N+1
stack = []
num = 1
for i in L:
    stack.append(i)
    if stack[-1] == num:
        stack.pop()
        num +=1
        if len(stack) !=0 and num != treshold:
            for i in range(len(stack)):
                if stack[-1] == num:
                    stack.pop()
                    num +=1
    elif num == treshold:
            break
    
if num == treshold:
    print('Nice')
else:
    print('Sad')

'''
한명씩 설수 있는 공간 -> 스택
한명 씩 스택에 넣음 -> for 문, append
한명씩 스택에 넣으면서 if 문으로 1번인지 확인
1번이라면 pop해서 제거하고  num +=1 해서 2번인지 확인할수 있도록 함.
남아있는 스택에서 다음 순서가 있는지 확인해야함
스택에 다 넣었으면 한명씩 뺴면서 다음 순서인지 확인 및 pop해야함
'''