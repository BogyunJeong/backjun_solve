def Search(find,arr): # 이분 탐색
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2 # 가운데 보기
        if arr[mid] == find:
            return 1
        elif arr[mid] < find: # 가운데 보다 찾는 값이 더 크면
            start = mid + 1
        else:
            end = mid - 1
    return 0



n = int(input())
A = list(map(int,input().split()))
m = int(input())
arr = list(map(int,input().split()))
A.sort()


for i in arr:
    print(Search(i,A))