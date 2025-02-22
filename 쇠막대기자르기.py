T = int(input())

for test_case in range(1,T+1):
    arr = list(input())
    result = 0

    stack = []
    for i in range(len(arr)):
        if arr[i] == '(' and arr[i+1] != ')': # 막대기라면
            razer = 0 # 레이저 개수 카운트
            op = 0 # 이거 다음에 막대기가 있는지 체크
            while True:
                i +=1
                if arr[i] == '(' and arr[i+1] != ')': # 또 막대기가 나온다면 체크
                    op +=1
                elif op != 0 and arr[i] == ')' and arr[i-1] != '(': # 다른 막대기 닫힘 
                    op -= 1
                elif arr[i] == '(' and arr[i+1] == ')': # 레이저라면 개수 체크
                    razer += 1
                elif op == 0 and razer != 0 and arr[i] == ')' and arr[i-1] != '(': # 지금 괄호가 닫혔다면
                    result += razer+1
                    break
    print(f'#{test_case} {result}')