T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    
    arr = [input().rstrip() for _ in range(N)]
    result = ""
    for i in range(N):
        for j in range(N-M+1):
            sub_arr = arr[i][j:j+M]
            if sub_arr == sub_arr[::-1]:
                result = "".join(sub_arr)
                
    for i in range(N-M+1):
        for j in range(N):
            sub_arr = [arr[K][j] for K in range(i,i+M)]
            if sub_arr == sub_arr[::-1]:
                result = "".join(sub_arr)


    print(f'#{test_case}',end = " ")
    for i in result:
        print(i,end="")
    print()




             
