T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = input() # str1
    p = input() # str2
     
    max_cnt = 0 #최대 개수를 저장할 변수
     
    for i in t: # str1을 반복a
        cnt = 0  # 몇개가 같은지 체크할 변수
        for j in p: # str2를 반복
            if i == j:  # 두 문자가 같다면
                cnt +=1 # 카운트
        if max_cnt < cnt:
            max_cnt = cnt
 
    print(f'#{test_case} {max_cnt}')