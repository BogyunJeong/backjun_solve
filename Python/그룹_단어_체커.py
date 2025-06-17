N = int(input())
cnt = N # 정답 카운트



for i in range(N):
    arr = input()

    for j in range(len(arr)-1):
        if arr[j] != arr[j+1]:
            if arr[j] in arr[j+1:]:
                cnt-=1
                break
        elif arr[j] == arr[j+1]:
            pass
print(cnt)
