import heapq
import sys

input = sys.stdin.readline

def insert_num(max_heap,min_heap,num):

    # 최대 힙이 비어있거나 추가할 값이 최대힙의 top 보다 작다면 최대힙에 추가
    if not max_heap or -max_heap[0] >= num:
        heapq.heappush(max_heap, -num) # 음수로 저장해줘야함
    else: 
        heapq.heappush(min_heap,num)

    # 균형 맞춰주기. // 둘의 길이 차이가 2 이상, // 최대 힙의 크기 < 최소 힙의 크기 일때
    if len(max_heap) > len(min_heap) + 1 :
        value = -heapq.heappop(max_heap) # 최대 힙에서 하나 빼서 최소 힙으로 넣어주기
        heapq.heappush(min_heap,value)
    elif len(max_heap) < len(min_heap):
        value = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -value)


max_heap = [] # 최대 힙은 음수로 저장
min_heap = []

n = int(input())
for i in range(1,n+1):
    num = int(input())
    insert_num(max_heap,min_heap,num)
    print(-max_heap[0]) 
