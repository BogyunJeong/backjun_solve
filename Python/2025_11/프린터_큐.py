from collections import deque

T = int(input())

for i in range(T):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))

    a = [[0] * 2 for _ in range(n)] # 배열을 [0,0]으로 만듬
    
    for i in range(len(arr)):  # arr 배열을 채워 넣음
        a[i][0] = arr[i]

    a[m][1] = -1 # 목표 배열을 1로 둠
    
    queue = deque(a)
    
    cnt = 0 # 순서 셀 카운트

    while(True):

        max_arr = max([first[0] for first in queue])

        out,check = queue.popleft()
        
        if max_arr == out: # 만약 중요도가 가장 높다면
            cnt += 1
            if check == -1: # 우리가 찾는 문서라면
                print(cnt) # 출력하고 루프 정지
                break

        else: # 중요도 높은게 아니라면 뒤에 다시 넣어야함
            queue.append([out,check])
            