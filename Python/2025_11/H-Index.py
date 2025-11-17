def solution(citations):
    # 정렬하기
    lst = sorted(citations)
    answer = 0

    # 정렬 했으니깐 0부터 체크하면 그게 최대값.

    for i in range(len(lst)):
        h = len(lst) - i
        if lst[i] >= h:
            return h
            
        
    return 0