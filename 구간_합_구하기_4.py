import sys
# 세그먼트 트리로 풀기
def update_tree(tree,start_idx,n):
    index = start_idx
    for i in range(n):
        idx = index + i
        while idx >= 1:
            tree[idx] += arr[i]
            idx//= 2
    return tree

def get_sub_tree_sum(left,right):
    sub_sum = 0
    while left < right:
        if left % 2 == 0:
            left //= 2
        else:
            sub_sum += tree[left]
            left = (left+1) // 2
        if right % 2 != 0:
            right //= 2
        else:
            sub_sum += tree[right]
            right = (right -1) // 2
        if left == right : sub_sum += tree[left]

    return sub_sum

N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
n = 0
while 2 ** n < N: n+=1
start_idx = 1 << n

tree = [0] * (N * 4)
tree = update_tree(tree,start_idx,N)

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    sum = get_sub_tree_sum(i+start_idx,j+start_idx)
    print(sum)

# 누적합
'''
N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
#전체 합 구하기
cnt = 0
allsum = [0]
for i in range(N):
    cnt += arr[i]
    allsum.append(cnt)


#부분 합 구하기
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    result = allsum[b] - allsum[a-1]
    print(result)
'''