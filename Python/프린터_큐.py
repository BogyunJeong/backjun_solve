from collections import deque

T = int(input())

for t in range(T):
    n,m = map(int,input().split())

    arr = list(map(int,input().split()))
    queue = deque(arr)

    cnt = 0

    while(True):
        arr_max = max(queue) # 현재 가장 높은 문서

        out = queue.popleft() # 가장 앞의 배열 숫자를 꺼냄
        if out != arr_max: # 꺼낸게 최대치가 아니라면 뒤에 다시 넣음
            arr.append(out)
        else:
            cnt += 1 # 순서 카운트
        if out == arr[m]: # 
            print(cnt)
            break


            

        
