N,M = map(int,input().split())
num = []
perm = [None] * M
used = [0] * N
for i in range(1,N+1):
    num.append(i)

def permutation(idx):
    if idx == M:
        for i in perm:
            print(i,end = " ")
        print()
        return
    
    for i in range(N):
        if not used[i]:  # 숫자가 사용되지 않았을 경우
            perm[idx] = num[i]  # 현재 위치에 숫자 저장
            used[i] = 1  # 숫자 사용 표시
            permutation(idx + 1)  # 다음 인덱스로 재귀 호출
            used[i] = 0  # 원래 상태로 되돌리기 (백트래킹)

permutation(0)