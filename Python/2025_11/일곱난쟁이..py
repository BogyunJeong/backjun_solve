from itertools import combinations

lst = []

for i in range(9):
    n = int(input())
    lst.append(n)

lst.sort()
comb = list(combinations(lst,7))

for i in comb:

    if sum(i) == 100:
        result = i
        for small in result:
            print(small, end = "\n")
        break


