N = int(input())

num = [i for i in range(1,N+1)]
cnt = 0
used_c = [0] * N # 같은 열 체크
used_x = [0] * (2*(N-1) +1) # y = x 체크
used_y = [0] * (2*(N-1) +1) # y = -x 체크

def permutation(idx):
    global cnt,N
    if idx == N:
        cnt += 1
        return
    for i in range(N):
        if not used_c[i] and not used_x[idx + i] and not used_y[(N-1) + idx - i]:
            used_c[i] = 1
            used_x[idx+i] = 1
            used_y[(N-1) + idx - i] = 1
            permutation(idx + 1)
            used_c[i] = 0
            used_x[idx+i] = 0
            used_y[(N-1) + idx - i] = 0


permutation(0)
print(cnt)

