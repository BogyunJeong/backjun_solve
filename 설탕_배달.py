N = int(input())
count = 0

if N % 5 == 0:
    print(N // 5)

else:
    while N >= 0:
        N -= 3
        count+=1
        if N % 5 == 0:
            count += N // 5
            print(count)
            break
        elif N == 1 or N == 2:
            print(-1)

