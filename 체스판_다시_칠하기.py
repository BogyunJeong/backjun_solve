N,M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(input())
result = []

for i in range(N-7):
    for j in range(M-7):
        b_count = 0
        w_count = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l) % 2 == 0: 
                    if arr[k][l] != 'W':
                        b_count +=1 # CASE 1번

                    if arr[k][l] != 'B':
                        w_count +=1 # CASE 2번
                        #1 짝수에 W가 아니라면?
                        #2 짝수에 B가 아니라면?
                else: 
                    if arr[k][l] != 'B':
                        b_count += 1 # CASE 1번
                    if arr[k][l] != 'W':
                        w_count+=1 # CASE 2번
 # 홀수에 B가 아니라면? 
 # 홀수에 W가 아니라면?
        result.append(w_count)
        result.append(b_count)
print(min(result))