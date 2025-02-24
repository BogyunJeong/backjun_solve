from math import inf
N = int(input())
arr = list(map(int,input().split()))
operator = list(map(int,input().split()))
# 연산자를 갯수별로 리스트를 만듬
O = [1] * operator[0] + [2] * operator[1] + [3] * operator[2] + [4] * operator[3]

max_result = -inf
min_result = inf
perm = [None] * len(O)
used = [0] * len(O)
def permutation(idx):
    global max_result,min_result
    if idx == len(O):
        result = arr[0]
        
        for i in range(1,len(arr)):
            if perm[i-1] == 1:
                result += arr[i]
            elif perm[i-1] == 2:
                result -= arr[i]
            elif perm[i-1] == 3:
                result *= arr[i]
            elif perm[i-1] == 4:
                if result < 0:
                    result = (-result // arr[i]) * -1
                else:
                    result //= arr[i]
     
        if result > max_result:
            max_result = result
        if result < min_result:
            min_result = result
        return
    for i in range(len(O)):
        if not used[i]:
            perm[idx] = O[i]
            used[i] = 1
            permutation(idx + 1)
            used[i] = 0

permutation(0)
print(max_result)
print(min_result)