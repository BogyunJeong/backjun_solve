lst = [0] * 31
for i in range(28):
    n = int(input())
    lst[n] = 1

for i in range(1,31):
    if not lst[i]:
        print(i)
