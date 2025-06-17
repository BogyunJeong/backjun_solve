arr = [2,7,5,3,1,4]
N = len(arr)
max_v = arr[0]
for i in range(1,N):
    if max_v < arr[i]:
        max_v = arr[i]

# 버블 정렬
a = [3,5,7,9,10,15,4]

def bubblesort(a,N):
    for i in range(N-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                print(a)        

bubblesort(a,len(a))

# 카운팅 정렬
Data = [4,6,1,3,2,7,10,8]
temp = [0] * max(Data)

def counting_sort(Data,Temp,k):
    Count = [0] * (k+1)
    for i in range(len(Data)):
        Count[Data[i]] += 1

    for i in range(1,k+1):
        Count[i] += Count[i-1]

    for i in range(len(Data)-1,-1,-1):
        Count[Data[i]] -= 1
        Temp[Count[Data[i]]] = Data[i]
        print(Temp,Count)

counting_sort(Data,temp,max(Data))

# 전치행렬
arr =[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(i):
        arr[i][j],arr[j][i] = arr[j][i],arr[i][j]

print(arr)

# 부분행렬
arr = [3,6,7,1,5,4]

n = len(arr)
for i in range(1<<n):
    for j in range(n):
        if i & (i << j):
            print(arr[j],end = " ")
    print()
print()

def binaryserh(a,N,key): # a는 배열 N은 배열 길이 key는 찾는 값값
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return middle
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1


def selectionsort(a,N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1,N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i],a[min_idx] = a[min_idx],a[i]