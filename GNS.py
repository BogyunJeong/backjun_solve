
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = input().split()
    arr = list(input().split())
    dict = {'ZRO' : 0,
            'ONE' : 0,
            'TWO' : 0,
            'THR' : 0,
            'FOR' : 0,
            'FIV' : 0,
            'SIX' : 0,
            'SVN' : 0,
            'EGT' : 0,
            'NIN' : 0
            }
    for i in arr:
        for j in dict.keys():
            if i == j:
                dict[j] +=1
    
    print(f'#{test_case}')

    for key,value in dict.items():
        for j in range(value):
            print(key,end = " ")